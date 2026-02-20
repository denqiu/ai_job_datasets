FROM python:3.14.3-slim
WORKDIR /ai_job_datasets
COPY requirements.txt .
RUN python -m venv venv && \
    venv/bin/pip install -r requirements.txt
