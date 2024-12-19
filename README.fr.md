# flask-boilerplate

## Description

Ce modèle de base est un point de départ solide pour créer des applications Flask prêtes à la production. Bien que conçu pour Flask, ses principes de base sont suffisamment polyvalents pour s'appliquer à d'autres frameworks et langages. Il s'agit notamment de maintenir une architecture propre, de mettre en œuvre une conception axée sur le domaine (DDD) et d'adhérer aux principes SOLID pour la conception orientée objet. Le projet intègre également les modèles CQRS (Command Query Responsibility Segregation) et DTO (Data Transfer Object), qui améliorent la gestion des données et la clarté du système. En adoptant le développement piloté par les tests (TDD), le boilerplate garantit un code fiable et de haute qualité. En appliquant ces meilleures pratiques, les développeurs peuvent créer des applications évolutives et faciles à maintenir, conformes aux normes modernes d'ingénierie logicielle.

## Badges

### Statut du projet

![CI Pipeline](https://github.com/cedric57/flask-boilerplate/actions/workflows/ci.yml/badge.svg)
![CD Pipeline](https://github.com/cedric57/flask-boilerplate/actions/workflows/cd.yml/badge.svg)
![Release](https://img.shields.io/badge/release-v1.0-blue)
[![License](https://img.shields.io/github/license/cedric57/flask-boilerplate)](https://github.com/cedric57/flask-boilerplate/blob/main/LICENSE)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-blue?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

### Langages utilisés

[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

### Qualité du code

[![Codecov](https://codecov.io/gh/cedric57/flask-boilerplate/branch/main/graph/badge.svg)](https://codecov.io/gh/user/repo)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Mypy](https://img.shields.io/badge/type%20checker-mypy-blue.svg)](http://mypy-lang.org/)

### Securité

![Dependabot](https://img.shields.io/badge/dependabot-enabled-blue?logo=dependabot&logoColor=white)

### Documentation

[![Documentation Status](https://readthedocs.org/projects/flask-boilerplate/badge/?version=latest)](https://flask-boilerplate.readthedocs.io)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/cedric57/flask-boilerplate/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-green.svg)](https://github.com/cedric57/flask-boilerplate/blob/main/README.fr.md)

### Contributions

[![cedric57 github](https://img.shields.io/badge/GitHub-cedric57-181717.svg?style=flat&logo=github)](https://github.com/cedric57)
![Contributors](https://img.shields.io/github/contributors/cedric57/flask-boilerplate)
![Last Commit](https://img.shields.io/github/last-commit/cedric57/flask-boilerplate)

## ⚡ Caractéristiques

- Gestion des dépendances et des paquets : [Poetry](https://python-poetry.org/)
- Hooks: [Pre-commit](https://github.com/pre-commit/pre-commit-hooks)
- Framework: [Flask](https://flask.palletsprojects.com/en/stable/)
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Format et Style: [Black](https://github.com/psf/black) + [ISort](https://pycqa.github.io/isort/) + [Flake8](https://github.com/PyCQA/flake8) + [MyPy](https://github.com/python/mypy)
- Tests: [Pytest](https://docs.pytest.org/en/stable/)
- Documentation: [Sphinx](https://www.sphinx-doc.org/en/master/)

## 👉 Table des matières
 
- [Pour commencer](#start)
- [Principes](#principles)
- [Structure des répertoires et organisation du code](#folder)
- [Ressources utiles](#resources)
- [Génération de types de clients](#client-types)

## <a name="start"></a>✨ Pour commencer

```bash
git clone https://github.com/cedric57/flask-boilerplate.git my-app
cd my-app

# Pour activer poetry, suivez les instructions ici : https://python-poetry.org/docs/#installing-with-the-official-installer
poetry install #Installer les dépendances.
```

### Commandes courantes

- `poetry install` - Installation avec poetry
- `poetry install --extras "web cli"` - Installation avec extras
- `poetry install --with dev` - Installation pour développement
- `poetry install --with docs` - Installation pour documentation
- `poetry run pytest` - Lancer les tests
- `poetry run black .` - Formatter le code
- `poetry run isort .` - Formatter le code
- `poetry run mypy .` - Vérifier les types
- `poetry run flask-boilerplate` - Lancer l'application
- `poetry add requests` - Ajout d'une dépendance
- `poetry add --group dev pytest` - Ajout d'une dépendance de dev

## <a name="principles"></a>🧱 Principes

## Contribuer

Les contributions sont toujours les bienvenues ! Si vous avez des idées, des suggestions, des corrections, n'hésitez pas à contribuer. Vous pouvez le faire en suivant les étapes suivantes :

1. Cloner ce repo
2. Créer une branche : `git checkout -b votre-fonctionnalité`
3. Faites quelques changements
4. Testez vos changements
5. Poussez votre branche et ouvrez une Pull Request

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
