import os
import requests

api_address = 'api'  # service name used in docker-compose network
api_port = 8000

# Authentication Test for 3 users
users = [
    ('alice', 'wonderland', 200),
    ('bob', 'builder', 200),
    ('clementine', 'mandarine', 403)
]

for username, password, expected_status in users:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': username,
            'password': password
        }
    )
    status_code = r.status_code

    output = f'''
===========================
    Authentication test
===========================
request done at "/permissions"
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
