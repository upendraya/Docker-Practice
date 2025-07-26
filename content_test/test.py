import os
import requests

api_address = 'api'
api_port = 8000

sentences = [
    ("life is beautiful", 1),
    ("that sucks", -1),
]

endpoints = ["/v1/sentiment", "/v2/sentiment"]

for sentence, expected_sign in sentences:
    for endpoint in endpoints:
        r = requests.get(
            url=f"http://{api_address}:{api_port}{endpoint}",
            params={'username': 'alice', 'password': 'wonderland', 'sentence': sentence}
        )
        try:
            score = r.json().get("score", 0)
            sign = 1 if score > 0 else -1
        except:
            sign = 0

        test_status = "SUCCESS" if sign == expected_sign else "FAILURE"
        output = f"""
============================
    Content Test
============================
request at {endpoint}
| sentence="{sentence}"
expected sign = {expected_sign}
actual score = {score}
==> {test_status}
"""
        print(output)
        if os.environ.get("LOG") == "1":
            with open("api_test.log", "a") as f:
                f.write(output)
