How to run:
1) Create docker network
```
>> docker network create recnet
```
2) Run database docker
```
>> screen -S database
>> cd database/docker
>> sh build_docker.sh
>> sh run_docker.sh
>> neo4j start
>> cypher-shell
>> login: neo4j; password: neo4j; new_password: test;
>> CREATE CONSTRAINT unique_id FOR ( n:Node ) REQUIRE (n.id) IS UNIQUE;
>> :exit
>> cd neo4j
>> python3 fill_database.py
>> cd ../
>> uvicorn database_api:database_app --host 0.0.0.0 --port 80 
>> Ctrl+d a
```
3) Run model, server and search_engine, client docker - model example below:
```
>> screen -S model
>> cd model/docker
>> sh build_docker.sh
>> sh run_docker.sh
>> copy and run command from README.md
>> Ctrl+d a
```
4) Read the IP of every docker from
```
>> docker network inspect recnet
```
and set the proper IP in every docker
5) Activate the client screen 
```
>> screen -r client
```
and check if you are getting recommendations
