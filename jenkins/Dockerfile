
FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y curl unzip python3 python3-pip git

RUN curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

USER jenkins
