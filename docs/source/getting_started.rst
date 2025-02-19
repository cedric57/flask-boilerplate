.. _getting-started:

Démarrage Rapide
================

.. contents:: Sommaire
   :depth: 2
   :local:

Prérequis
---------
- Python 3.12+
- Poetry 1.8+
- PostgreSQL 15+ (ou SQLite pour le développement)

Installation
------------
.. code-block:: bash

    # Cloner le dépôt
    git clone https://github.com/cedric57/flask-boilerplate.git
    cd flask-boilerplate

    # Installer les dépendances
    poetry install --with dev

Configuration
-------------
1. Créer le fichier `.env` :

.. code-block:: ini
    :caption: .env

    FLASK_APP=app
    FLASK_ENV=development
    DATABASE_URL=postgresql://user:password@localhost/db_name
    SECRET_KEY=your-secret-key

2. Initialiser la base de données :

.. code-block:: bash

    poetry run flask db init       # Initialiser Alembic
    poetry run flask db migrate    # Créer une migration
    poetry run flask db upgrade    # Appliquer les migrations

Lancer l'Application
--------------------
.. code-block:: bash

    # Mode développement
    poetry run flask run --port 5000

    # Ou avec le rechargement automatique
    poetry run flask run --reload

Structure du Projet
-------------------
.. code-block:: text

    .
    ├── app/
    │   ├── __init__.py
    │   ├── api/           # Blueprints API
    │   ├── models/        # Modèles SQLAlchemy
    │   ├── core/          # Configuration
    │   └── utils/         # Helpers
    ├── migrations/        # Fichiers Alembic
    ├── tests/             # Tests Pytest
    └── pyproject.toml     # Configuration Poetry

Commandes Utiles
----------------
.. list-table::
   :header-rows: 1

   * - Commande
     - Description
   * - ``poetry run pytest``
     - Lancer tous les tests
   * - ``poetry run flask shell``
     - Shell contextuel Flask
   * - ``poetry run celery -A app worker``
     - Lancer Celery worker (si activé)

Prochaines Étapes
-----------------
- Explorer la :doc:`documentation API <modules>`
- Personnaliser la configuration dans ``app/core/config.py``
- Ajouter des endpoints dans ``app/api/``

.. note::
    Pour la configuration de production, voir le guide de déploiement dans la documentation avancée.

.. toctree::
   :hidden:

   introduction
   modules
