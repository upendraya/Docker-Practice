import os
import requests

api_address = 'api'
api_port = 8000

tests = [
    ("alice", "wonderland", "/v1/sentiment", 200),
    ("alice", "wonderland", "/v2/sentiment", 200),
    ("bob", "builder", "/v1/sentiment", 200),
    ("bob", "builder", "/v2/sentiment", 403),
]

for username, password, endpoint, expected in tests:
    r = requests.get(
        url=f"http://{api_address}:{api_port}{endpoint}",
        params={'username': username, 'password': password, 'sentence': 'test'}
    )
    status_code = r.status_code
    test_status = "SUCCESS" if status_code == expected else "FAILURE"
    output = f"""
============================
    Authorization test
============================
request at {endpoint}
| username="{username}"
| password="{password}"
expected result = {expected}
actual result = {status_code}
==> {test_status}
"""
    print(output)
    if os.environ.get("LOG") == "1":
        with open("api_test.log", "a") as f:
            f.write(output)
