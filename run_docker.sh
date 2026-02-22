#!/bin/bash
# In local environment, load env variables. In GitHub Actions, env variables are already loaded in workflow and .env doesn't exist because of .gitignore.
# In short, if .env exists, source it, otherwise, assume remote and variables already loaded so no need to source remotely.
[ -f .env ] && source .env
# docker compose up switches image to the latest one and replace previous image with <none> tag
docker compose up --remove-orphans
# Then finds images with <none> tag, known as dangling images. Does not work before docker compose up.
docker image prune -f
# Note '-' prefixing creatordate to show sort in descending order, finding the latest tag.
[ -f .env ] && TAG=$(git tag --sort=-creatordate | head -n 1)
mkdir -p output
docker cp ${DOCKER_CONTAINER}:/app/numpy_ai_job_datasets.csv ./output/numpy_ai_job_datasets_${TAG}.csv
