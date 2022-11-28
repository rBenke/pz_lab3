FROM ubuntu:22.04

RUN apt-get update -y

RUN apt-get install python3-pip -y

RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

RUN apt-get install vim -y

RUN pip3 install torch
RUN pip3 install numpy
RUN pip3 install -U scikit-learn

RUN pip3 install torch-scatter torch-sparse -f https://data.pyg.org/whl/torch-1.13.0+cpu.html 
RUN pip3 install torch-geometric -f https://data.pyg.org/whl/torch-1.13.0+cpu.html 

RUN pip3 install ogb

WORKDIR /app
ENTRYPOINT /bin/bash


