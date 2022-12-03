FROM ubuntu:20.04
ENV PYTHONUNBUFFERED=1
RUN apt update
RUN apt-get install -y python3 && ln -sf python3 /usr/bin/python
RUN apt install -y python3-venv
RUN apt install -y python3-pip
WORKDIR /cds-infrastructure
COPY . .
RUN pip3 install --no-cache --upgrade pip setuptools
