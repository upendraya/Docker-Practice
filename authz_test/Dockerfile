FROM python:3.9

WORKDIR /app

COPY test.py .

RUN pip install --no-cache-dir --disable-pip-version-check --progress-bar=off requests

# Remove any directory named api_test.log to avoid conflict
RUN rm -rf /app/api_test.log

CMD ["python", "test.py"]
