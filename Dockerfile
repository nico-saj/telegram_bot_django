# Base stage for dependencies
FROM python:3.12.6-slim as base

# Set up environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PIPENV_VENV_IN_PROJECT=1
# Set Pipenv to create the virtual environment in the project directory

# Install pipenv and dependencies
RUN apt-get update && apt-get install -y \
    --no-install-recommends gcc \
    build-essential \
    libpq-dev \
    postgresql-server-dev-all \
    && pip install pipenv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Work in the app directory and install dependencies
WORKDIR /app
COPY Pipfile* ./
RUN pipenv install --deploy --ignore-pipfile

# Application stage
FROM python:3.12.6-slim as runtime

# Install pipenv in the runtime environment
RUN apt-get update && apt-get install -y \
    --no-install-recommends libpq-dev \
    && pip install pipenv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the application files and virtual environment from the base stage
WORKDIR /app
COPY --from=base /app /app
COPY . .

# Set PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Create a non-root user to run the application
RUN useradd --create-home appuser
USER appuser

# Command to run the bot
CMD ["pipenv", "run", "python", "manage.py", "run_telegram_bot"]
