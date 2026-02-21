# Dataset Analysis on the Job Market in AI/Machine Learning

**Project assignment for Module 6 in course CTI-110 at Wake Tech (WTCC).**

Used Power Query to clean up data. But it was slow so logic was migrated to numpy. Then used Docker to take care of Python environment. Didn't feel like installing the latest version of Python on my computer.

## To run if Python is not installed:

1. Install Docker
2. <code>docker compose up</code>

This will run Dockerfile, execute the api, and export csv to output folder.

Note: I don't think Docker is necessary for the project.

## If Python is installed:

You can run the UI, select datasets from Module 5, and export csv to output folder.

<code>run_ui.cmd</code>

## To learn how to use docker commands:

See <code>docker-commands.md</code>.
