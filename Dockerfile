# Étape de construction
FROM python:3.12-slim as builder

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances
COPY pyproject.toml poetry.lock ./

# Installation de Poetry
ENV POETRY_VERSION=1.8.2
RUN pip install --user "poetry==$POETRY_VERSION"

# Installation des dépendances Python
ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Étape finale
FROM python:3.12-slim

WORKDIR /app

# Copie des artefacts de l'étape builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

# Configuration de l'application
ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app/src

# Exposition du port
EXPOSE 5000

# Utilisateur non-root
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "src.app:create_app()"]
