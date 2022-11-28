docker run --rm -it \
	--network recnet \
	-v $(pwd)/../app:/app \
	-v $(pwd)/../data:/data \
	--env NEO4J_AUTH=neo4j/test \
	--name database_docker database_img
