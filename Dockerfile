
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt



FROM python:3.11-slim

WORKDIR /app


COPY --from=builder /install /usr/local


COPY ./app ./app

EXPOSE 8000


CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
