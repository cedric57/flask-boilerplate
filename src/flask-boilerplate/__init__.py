from flask import Flask

def create_app():
    """
    Factory function to create and configure the Flask application.
    
    This function sets up the Flask application instance with necessary configurations,
    registers blueprints, initializes extensions, and sets up error handlers.
    
    Returns:
        app (Flask): The configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Load configuration settings from the config module
    app.config.from_object('config.Config')
    
    # Register blueprints for modular application structure
    from .blueprints import register_blueprints
    register_blueprints(app)
    
    # Initialize extensions like database, authentication, etc.
    from .extensions import init_extensions
    init_extensions(app)
    
    # Register error handlers for custom error pages and logging
    from .error_handlers import register_error_handlers
    register_error_handlers(app)
    
    return app
