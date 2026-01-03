FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy dependency files from the ROOT context
COPY pyproject.toml poetry.lock* ./

# Install ONLY backend dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --with test

# Copy the backend source code
COPY backend ./backend

CMD ["uvicorn", "backend.src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]