# Sentiment API Test Pipeline
A team has created an application that allows to use a sentiment analysis algorithm: it allows to predict if a sentence is positive or negative. This API will be deployed in a container whose image is for the moment datascientest/fastapi:1.0.0. 

This project implements a CI/CD pipeline to automatically test a sentiment analysis API deployed in Docker containers. The API supports multiple endpoints for status, user permissions, and sentiment analysis using two model versions.

The goal is to create automated tests for:

- Authentication: Validate user login credentials.
- Authorization: Verify access control for different API versions.
- Content: Check correctness of sentiment analysis results.
