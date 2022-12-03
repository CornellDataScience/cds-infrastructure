FROM alpine:latest
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
WORKDIR /cds-infrastructure
COPY . .
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flake8
RUN pip3 install autopep8
RUN pip3 install pytest
RUN pip3 install pyyaml
