#!/bin/bash
# In local environment, load env variables. In GitHub Actions, env variables are already loaded in workflow and .env doesn't exist because of .gitignore.
# In short, if .env exists, source it, otherwise, assume remote and variables already loaded so no need to source remotely.
[ -f .env ] && source .env
docker image prune -f
docker compose up --remove-orphans
docker cp ${DOCKER_CONTAINER}:/app/numpy_ai_job_datasets.csv ./numpy_ai_job_datasets.csv
