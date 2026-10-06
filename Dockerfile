# syntax=docker/dockerfile:1

FROM python:3.14-slim

LABEL version="2.0.0"
LABEL description="Example processing of YAML file"
LABEL author="Frank H Jung"

WORKDIR app

RUN pip install --no-cache-dir pyyaml>=6.0.3

ADD  employees employees
ADD  utils utils

COPY logger.properties .
COPY read_yaml.py .

ENTRYPOINT ["./read_yaml.py"]

CMD ["--help"]
