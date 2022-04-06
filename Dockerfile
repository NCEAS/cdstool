FROM ubuntu:20.04

RUN apt update && \
    apt install -y python3.9 python3.9-venv python3.9-distutils curl bind9-host netcat-openbsd

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

RUN python3.9 get-pip.py

RUN pip install parsl
