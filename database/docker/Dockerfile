FROM neo4j:5.2.0-community

RUN apt-get update -y

RUN apt-get install python3-pip -y

RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

RUN apt-get install vim -y

RUN pip3 install py2neo

RUN pip3 install ogb
RUN apt-get install curl -y


WORKDIR /app
ENTRYPOINT /bin/bash


