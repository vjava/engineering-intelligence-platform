
# Engineering Intelligence Platform

Flow:

Git -> Jenkins (Docker) -> Databricks Bundle Validate -> Deploy -> Run Job

## Prerequisites

- Docker Desktop
- Git
- Databricks CLI
- Databricks Workspace
- Jenkins in Docker

## Start Jenkins

docker compose up -d

Open:
http://localhost:8080

## Configure Credentials

Create Jenkins Secret Text credentials:

DATABRICKS_HOST
DATABRICKS_TOKEN

## Pipeline

Push code to Git.
Create Jenkins Pipeline from SCM.
Point to jenkins/Jenkinsfile.

Build Now.

## Manual Local Test

databricks bundle validate
databricks bundle deploy
databricks bundle run engineering_intelligence_job
