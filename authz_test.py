import os
import requests

api_address = 'api'  # matches your docker-compose service name
api_port = 8000

# Users and expected access for /v1/sentiment and /v2/sentiment
tests = [
    ('alice', 'wonderland', '/v1/sentiment', 200),
    ('alice', 'wonderland', '/v2/sentiment', 200),
    ('bob', 'builder', '/v1/sentiment', 200),
    ('bob', 'builder', '/v2/sentiment', 403),
]

for username, password, endpoint, expected_status in tests:
    r = requests.get(
        url=f'http://{api_address}:{api_port}{endpoint}',
        params={
            'username': username,
            'password': password,
            'sentence': 'test sentence'
        }
    )
    status_code = r.status_code

    output = f'''
===========================
    Authorization test
===========================
request done at "{endpoint}"
| username="{username}"
| password="{password}"
expected result = {expected_status}
actual result = {status_code}
==> {'SUCCESS' if status_code == expected_status else 'FAILURE'}
'''

    print(output)

    if os.environ.get("LOG") == "1":
        with open("api_test.log", "a") as log_file:
            log_file.write(output)
