FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /api-1

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy the current directory contents into the container at /hello-world
COPY ./api-1/pyproject.toml ./api-1/poetry.lock /api-1/

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copy the rest of your consumer's source code from your host to your image filesystem.
COPY ./api-1 /api-1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

/shopping

/login

/cart