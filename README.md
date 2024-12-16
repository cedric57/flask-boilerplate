# flask-boilerplate

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/cedric57/flask-boilerplate/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-green.svg)](https://github.com/cedric57/flask-boilerplate/blob/main/README.fr.md)
[![MIT License](https://img.shields.io/github/license/cedric57/flask-boilerplate)](https://github.com/cedric57/flask-boilerplate/blob/main/LICENSE)

This boilerplate is a robust starting point for creating production-ready Flask applications. Although tailored for Flask, its core principles are versatile enough for other frameworks and languages. These include maintaining clean architecture, implementing domain-driven design (DDD), and adhering to the SOLID principles for object-oriented design. The project also incorporates the Command Query Responsibility Segregation (CQRS) and Data Transfer Object (DTO) patterns, which enhance data management and system clarity. Embracing test-driven development (TDD), the boilerplate ensures high-quality, reliable code. By applying these best practices, developers can create scalable, maintainable applications that align with modern software engineering standards.

## ⚡ Features

- Dependency and package management: [Poetry](https://python-poetry.org/)

## 👉 Table of Contents

- [Getting Started](#start)
- [Principles](#principles)
- [Folder Structure and Code Organization](#folder)
- [Useful resources](#resources)
- [Client types generation](#client-types)

## <a name="start"></a>✨ Getting Started

```bash
git clone https://github.com/cedric57/flask-boilerplate.git my-app
cd my-app

# To enable poetry follow the instruction here: https://python-poetry.org/docs/#installing-with-the-official-installer
poetry install #Install dependencies.
```

### Common Commands

- `poetry install` - Installation with poetry
- `poetry install --extras "web cli"` - Installation with extras
- `poetry install --with dev` - Installation for development
- `poetry install --with docs` - Installation for documentation
- `poetry run pytest` - Run tests
- `poetry run black .` - Format the code
- `poetry run isort .` - Format the code
- `poetry run mypy .` - Check types
- `poetry run flask-boilerplate` - Start application
- `poetry add requests` - Add a dependency
- `poetry add --group dev pytest` - Add a dev dependency

## <a name="principles"></a>🧱 Principles

## <a name="folder"></a>🗄️ Folder Structure and Code Organization

## <a name="resources"></a>Useful resources

## <a name="client-types"></a>Client types generation

## Contributing

Contributions are always welcome! If you have any ideas, suggestions, fixes, feel free to contribute. You can do that by going through the following steps:

1. Clone this repo
2. Create a branch: `git checkout -b your-feature`
3. Make some changes
4. Test your changes
5. Push your branch and open a Pull Request

## License

[MIT](https://choosealicense.com/licenses/mit/)
