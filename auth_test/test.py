import os
import requests

api_address = 'api'
api_port = 8000

users = [
    ("alice", "wonderland", 200),
    ("bob", "builder", 200),
    ("clementine", "mandarine", 403),
]

for username, password, expected in users:
    r = requests.get(
        url=f"http://{api_address}:{api_port}/permissions",
        params={'username': username, 'password': password}
    )
    status_code = r.status_code
    test_status = "SUCCESS" if status_code == expected else "FAILURE"
    output = f"""
============================
    Authentication test
============================
request at /permissions
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
