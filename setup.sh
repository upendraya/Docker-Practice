#!/bin/bash
# Build test containers
docker-compose build

# Run the tests (stop if any container fails)
docker-compose up --abort-on-container-exit
