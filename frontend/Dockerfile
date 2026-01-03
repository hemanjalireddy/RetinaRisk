FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

# Install ONLY frontend dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --with test

COPY frontend ./frontend

CMD ["streamlit", "run", "frontend/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]