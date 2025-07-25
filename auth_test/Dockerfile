FROM python:3.9

WORKDIR /app

COPY test.py .
COPY requirements.txt .

# Set low-resource env flags
ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_PROGRESS_BAR=off \
    PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

CMD ["python", "test.py"]
