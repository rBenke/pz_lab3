FROM ubuntu:22.04

RUN apt-get update -y

RUN apt-get install python3-pip -y

RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

RUN apt-get install vim -y

RUN pip3 install faiss-cpu

RUN pip3 install numpy
RUN pip3 install torch
WORKDIR /app
ENTRYPOINT /bin/bash


