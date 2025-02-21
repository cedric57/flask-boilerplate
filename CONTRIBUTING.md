# Contribution Guide

Merci de votre intérêt pour contribuer à Flask Boilerplate ! 🚀

Voici les directives pour contribuer efficacement au projet.

## Environnement de développement

### Prérequis

- Python 3.12+
- [Poetry](https://python-poetry.org/) (gestion des dépendances)
- Git
- make (pour la génération de documentation)

### Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/cedric57/flask-boilerplate.git
cd flask-boilerplate
```

1. Installer les dépendances avec Poetry :

```bash
poetry install
```

1. Activer l'environnement virtuel géré par Poetry :

```bash
poetry shell
```

1. Installer les hooks pre-commit :

```bash
poetry run pre-commit install
```

1. Configurer les variables d'environnement :

```bash
cp.env.example .env
```

## Guidelines de contribution

### 🐛 Signaler un bug

1. Vérifier les [issues existantes](https://github.com/cedric57/flask-boilerplate/issues)

1. Créer une nouvelle issue avec :

- Titre descriptif
- Description détaillée
- Étapes pour reproduire le bug
- Comportement attendu vs actuel
- Captures d'écran (si applicable)
- Environnement (OS, version Python, etc.)
- Solution potentielle (si connue)
-

### 💡 Proposer une fonctionnalité

1. Vérifier les [roadmap existantes](https://github.com/cedric57/flask-boilerplate/issues)

1. Décrire :

- Le problème à résoudre
- La solution proposée
- Alternatives envisagées
- Documentation pertinente

### 🛠 Soumettre une Pull Request

1. Créer une branche :

```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

1. Suivre les standards :

- Exécuter les hooks pre-commit (vérification automatique)
- Vérifier le style de code avec Ruff (voir section dédiée)
- Ajouter des tests unitaires
- Mettre à jour la documentation
- Garder les commits atomiques

1. Pousser les changements :

```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

1. Ouvrir une Pull Request sur GitHub avec :

- Description des changements
- Captures d'écran (si applicable)
- Référence aux issues concernées

## Outils de développement

### Hooks pre-commit

Le projet utilise des hooks Git pré-commit pour :

- Vérifier le formatage avec Ruff
- Détecter les secrets dans le code
- Vérifier la syntaxe YAML/JSON
- Empêcher les fichiers de grande taille

Les hooks s'exécutent automatiquement à chaque commit. Pour exécuter manuellement :

```bash
poetry run pre-commit run --all-files
```

Configuration : [.pre-commit-config.yaml](https://chat.deepseek.com/a/chat/s/.pre-commit-config.yaml)

## Style de code

- Python : Ruff (formatage + linting)

```bash
poetry run ruff check .  # Vérification
poetry run ruff format .  # Auto-formatage
```

- Documentation : Google-style docstrings
- Fichiers de configuration : YAML/JSON indenté
- Exécution automatique via pre-commit
- Configuration Ruff : [pyproject.toml](https://chat.deepseek.com/a/chat/s/pyproject.toml)

## Documentation

### Génération avec Sphinx

1. Installer les dépendances de documentation :

```bash
poetry add --group dev sphinx sphinx-rtd-theme myst-parser
```

1. Générer la documentation :

```bash
cd docs
make html
```

1. Consulter la documentation générée :

```bash
open _build/html/index.html
```

Conventions :

- Utiliser des docstrings Google-style
- Documenter toutes les API publiques
- Mettre à jour les fichiers .rst dans /docs/source

### Mise à jour de la documentation

- README.md
- CHANGELOG.md
- Docstrings
- Wiki (si applicable)

## Tests

Avant de soumettre :

```bash
pytest tests/ --cov=app --cov-report=term-missing
```

## Gestion des dépendances

Ajouter une dépendance :

```bash
poetry add package-name
```

Ajouter une dépendance de développement :

```bash
poetry add --group dev package-name
```

Synchroniser l'environnement :

```bash
poetry install --sync
```

## Code de Conduite

Respecter les [GitHub Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)

## Questions ?

Contactez les mainteneurs :

- Cédric [@cedric57](https://github.com/cedric57)
- Via les [GitHub Discussions](https://github.com/cedric57/flask-boilerplate/discussions)

Merci pour votre contribution ! 🙌
