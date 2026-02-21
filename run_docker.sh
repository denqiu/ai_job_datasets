#!/bin/bash
source .env
docker image prune -f
docker compose up --remove-orphans
docker cp ${DOCKER_CONTAINER}:/app/numpy_ai_job_datasets.csv ./numpy_ai_job_datasets.csv
