FROM python:3.9-slim

# Disable pip threading and rich output
ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_PROGRESS_BAR=off \
    PYTHONUNBUFFERED=1 \
    RICH_NO_ENVIRON=1 \
    RICH_NO_COLOR=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --disable-pip-version-check --progress-bar=off requests

CMD ["python", "test.py"]
