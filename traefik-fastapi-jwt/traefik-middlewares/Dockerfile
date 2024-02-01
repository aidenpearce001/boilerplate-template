FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /traefik-middleware

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy the current directory contents into the container at /hello-world
COPY ./traefik-middleware/pyproject.toml ./traefik-middleware/poetry.lock /traefik-middleware/

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copy the rest of your consumer's source code from your host to your image filesystem.
COPY ./traefik-middleware /traefik-middleware

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
