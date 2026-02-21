# Dataset Analysis on the Job Market in AI/Machine Learning

**Project assignment for Module 6 in course CTI-110 at Wake Tech (WTCC).**

Datasets were curled from Kaggle. Used Power Query to clean up data. But it was slow so logic was migrated to numpy. Then used Docker to take care of Python environment. Didn't feel like installing the latest version of Python on my computer.

## Without Docker or Python installed:

### Releases

1. Run <code>create-tag.sh</code> to create and push a new tag.
2. New workflow is triggered on tag.
3. Download release.

### Artifacts

**Issue (Resolved): [Artifact Download Not Working](https://github.com/denqiu/ai_job_datasets/issues/6)**

There are 2 ways to do this:

1. Recently added workflow_dispatch. Go to Actions > Run Workflow > Select branch > Run Workflow.
2. Simply go to Actions > job with green checkmark > Summary > Artifacts > download csv to Downloads folder. Right+click > save link as > choose folder to download csv to.

## (With Docker) To run if Python is not installed:

1. Install Docker
2. <code>docker compose up</code>

This will run Dockerfile, execute the api, and export csv to output folder.

Note: I don't think Docker is necessary for the project.

## If Python is installed:

You can run the UI, select datasets from Module 5, and export csv to output folder.

<code>run_ui.cmd</code>

## To learn how to use docker commands:

See <code>docker-commands.md</code>.
