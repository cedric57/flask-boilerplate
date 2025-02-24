# Politique de Sécurité du Projet Flask Boilerplate

Ce document décrit les politiques de sécurité et les procédures à suivre pour signaler et gérer les vulnérabilités ou les incidents de sécurité dans le projet **flask-boilerplate**.

## ⚠️ Signaler une Vulnérabilité

Nous prenons la sécurité de ce projet très au sérieux. Si vous découvrez une vulnérabilité, merci de nous en informer **de manière responsable** en suivant les étapes ci-dessous :

### 1. Évaluation Initiale

Avant de signaler une vulnérabilité, assurez-vous que :

- La vulnérabilité n'est pas déjà documentée dans les problèmes (issues) ou les discussions (discussions) du dépôt.
- Vous avez reproduit la vulnérabilité dans un environnement contrôlé.

### 2. Contact

**Méthode de signalement préférée** :
👉 Utilisez les [Security Advisories GitHub](https://github.com/cedric57/flask-boilerplate/security/advisories/new)

**Alternative (pour les rapports sensibles)** :
📧 Envoyez un email à [cedricgrun+security@gmail.com](mailto:cedricgrun+security@gmail.com) avec pour objet "[SECURITY] Flask Boilerplate"
🔒 *Option de chiffrement :* [Clé GPG publique](https://keys.openpgp.org/)

### 3. Informations à Fournir

Lorsque vous nous envoyez un rapport de vulnérabilité, veuillez inclure les informations suivantes :

- **Titre de la Vulnérabilité** : Une description concise de la vulnérabilité.
- **Description Détailée** : Une explication détaillée de la vulnérabilité, y compris les étapes pour la reproduire.
- **Impact** : Une description de l'impact potentiel de la vulnérabilité.
- **Correctif Proposé** : Si possible, proposez un correctif ou une solution pour résoudre la vulnérabilité.
- **Coordonnées de Contact** : Votre nom et adresse email pour que nous puissions vous recontacter si nécessaire.

### 4. Confidentialité

Nous traiterons toutes les informations que vous nous fournirez de manière confidentielle et ferons tout effort pour résoudre la vulnérabilité rapidement.

### 5. Reconnaissance

Nous remercions tous ceux qui nous aident à améliorer la sécurité de notre projet. Nous pouvons vous offrir une reconnaissance publique dans le fichier `SECURITY_HALL_OF_FAME.md` si vous le souhaitez.

## 🔄 Processus de Réponse

| Étape               | Délai                  | Actions                                    |
| ------------------- | ---------------------- | ------------------------------------------ |
| Accusé de réception | Sous 3 jours ouvrables | Confirmation de réception du rapport       |
| Validation          | Sous 7 jours           | Vérification technique de la vulnérabilité |
| Correctif développé | Sous 30 jours\*        | Création et test du correctif              |
| Publication         | Selon criticité        | Release sécurisée avec crédits             |

*\*Délais variables selon la complexité*

## Périmètre Couvert

### 🎯 En Scope

- Code du dépôt principal (`/src`)
- Configuration par défaut
- Dépendances principales (Flask, SQLAlchemy, etc.)
- Documentation officielle

### 🚫 Hors Scope

- Fork personnels du projet
- Dépendances optionnelles (Celery, Redis, etc.)
- Problèmes sans preuve d'exploitation concrète
- Vulnérabilités nécessitant une configuration non standard

## 🛠️ Outils de Sécurité Utilisés

Ce projet utilise plusieurs outils de sécurité pour détecter et prévenir les vulnérabilités :

### 1. CodeQL

- **Description** : CodeQL est un outil de recherche de vulnérabilités qui utilise une langue de requête pour analyser le code source.
- **Configuration** : Les analyses CodeQL sont exécutées automatiquement sur les branches `main`, `develop`, `feature/**`, `release/**`, et `hotfix/**`.
- **Workflow** : [codeql-analysis.yml](.github/workflows/codeql-analysis.yml)

### 2. Bandit

- **Description** : Bandit est un outil de sécurité pour analyser le code Python et détecter des vulnérabilités potentielles.
- **Configuration** : Bandit est intégré dans les hooks `pre-commit` pour s'exécuter avant chaque commit et pull request.
- **Workflow** : [ci-feature.yml](.github/workflows/ci-feature.yml)

### 3. pre-commit

- **Description** : pre-commit est un outil qui exécute des hooks de pré-commit pour valider le code avant qu'il ne soit ajouté au dépôt.
- **Configuration** : Les hooks `pre-commit` incluent des outils de sécurité comme Bandit, des validateurs de code comme Ruff, et des formateurs comme Prettier.
- **Workflow** : [ci-feature.yml](.github/workflows/ci-feature.yml)

### 4. Coverage et Codecov

- **Description** : Les outils de couverture de code (comme pytest-cov) et Codecov permettent de mesurer la couverture des tests et d'identifier les parties non testées du code.
- **Configuration** : Les rapports de couverture sont générés et envoyés à Codecov après chaque exécution des tests unitaires.
- **Workflow** : [ci-feature.yml](.github/workflows/ci-feature.yml)

## 🛡️ Bonnes Pratiques de Sécurité

Ce boilerplate intègre déjà :

- Configuration sécurisée par défaut pour Flask
- Protection contre les attaques CSRF
- Gestion sécurisée des secrets via `.env`
- Headers HTTP sécurisés (CSP, HSTS, etc.)
- Validation des entrées avec Pydantic

Pour maintenir la sécurité :

```bash
# Mettez à jour régulièrement les dépendances
poetry update --dry-run  # Vérifiez les mises à jour
poetry update  # Appliquez les mises à jour
```

### 1. Utilisation de Commitizen et Conventional Commits

- **Description** : Commitizen et Conventional Commits aident à standardiser les messages de commit, ce qui facilite la traçabilité et la gestion des changements.
- **Configuration** : Les messages de commit sont validés automatiquement pour respecter les conventions.
- **Workflow** : [ci-feature.yml](.github/workflows/ci-feature.yml)

### 2. Utilisation de pre-commit.ci

- **Description** : pre-commit.ci exécute automatiquement les hooks `pre-commit` sur chaque pull request et peut corriger certaines vulnérabilités.
- **Configuration** : Les hooks `pre-commit` sont configurés pour s'exécuter sur `pre-commit.ci`.
- **Workflow** : [ci-feature.yml](.github/workflows/ci-feature.yml)

### 3. Exclusions dans les Rapports de Couverture

- **Description** : Les fichiers et répertoires spécifiques (comme les fichiers `__init__.py`, les tests, et les répertoires de primitives) sont exclus des rapports de couverture pour éviter les faux positifs.
- **Configuration** : Les exclusions sont définies dans le fichier [codecov.yml](codecov.yml).

## 📦 Gestion des Mises à Jour de Sécurité

Les corrections critiques sont publiées via :

- [GitHub Releases](https://github.com/cedric57/flask-boilerplate/releases)
- [GitHub Security Advisories](https://github.com/cedric57/flask-boilerplate/security/advisories)
- [CVE Database](https://cve.mitre.org/) (pour les vulnérabilités critiques)

## Politiques de Confidentialité

- **Confidentialité des Rapports** : Toutes les informations fournies dans les rapports de vulnérabilité seront traitées de manière confidentielle.
- **Publicité des Corrections** : Une fois la vulnérabilité corrigée, nous publierons une mise à jour du projet et mettrons à jour les notes de version.
- **Reconnaissance** : Si vous souhaitez une reconnaissance publique, nous vous enverrons une notification une fois que la mise à jour est publiée.

## 🙏 Remerciements

Nous reconnaissons volontiers les contributions à la sécurité :

- [Liste des chercheurs en sécurité](https://github.com/cedric57/flask-boilerplate/SECURITY_HALL_OF_FAME.md)
  Vous souhaitez figurer ici ? Indiquez-le dans votre rapport !
