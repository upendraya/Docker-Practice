import os
import requests

api_address = 'api'  # Docker service name for the API
api_port = 8000

# Sentences to test with expected sentiment signs
test_sentences = [
    ("life is beautiful", 1),
    ("that sucks", -1),
]

# Endpoints to test
endpoints = ["/v1/sentiment", "/v2/sentiment"]

for endpoint in endpoints:
    for sentence, expected_sign in test_sentences:
        r = requests.get(
            url=f"http://{api_address}:{api_port}{endpoint}",
            params={
                "username": "alice",
