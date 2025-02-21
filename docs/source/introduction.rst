.. _introduction:

Introduction au Projet
======================

.. image:: https://img.shields.io/badge/flask-%23000.png?style=for-the-badge&logo=flask&logoColor=white
    :target: https://flask.palletsprojects.com/
    :alt: Flask Badge

Un boilerplate moderne pour applications Flask avec les fonctionnalités essentielles pré-configurées.

Présentation
------------
Ce projet est une base de démarrage pour :

* Développement rapide d'API REST
* Applications web traditionnelles avec templates
* Microservices modulaires

Fonctionnalités Clés
--------------------
.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Module
     - Description
   * - **Authentification**
     - JWT, OAuth2 prêt à l'emploi
   * - **Base de Données**
     - SQLAlchemy + Alembic migrations
   * - **Configuration**
     - Environnements multiples (dev/prod/test)
   * - **Logging**
     - Configuration centralisée
   * - **Tests**
     - Pytest avec fixtures

Stack Technique
---------------
.. code-block:: text

    Python 3.12
    Flask 3.1
    SQLAlchemy 2.0
    Pydantic 2.7
    Celery 5.3 (optionnel)

Démarrer un Développement
-------------------------
Exemple de création d'endpoint :

.. code-block:: python

    from app.api import api_bp

    @api_bp.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200

.. note::
    Pré-requis :
    - Python 3.12+ installé
    - Poetry pour la gestion des dépendances

Pour une configuration complète, voir :doc:`getting_started`.

Architecture du Projet
----------------------
.. code-block:: bash

    .
    ├── app/
    │   ├── api/          # Endpoints
    │   ├── core/         # Configuration
    │   ├── models/       # Modèles DB
    │   └── utils/        # Helpers
    └── tests/           # Tests
