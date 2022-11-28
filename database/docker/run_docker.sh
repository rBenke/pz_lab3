docker run --rm -it \
	--network recnet \
	-v /home/rbenke/repo/recSys/database/app:/app \
	-v /home/rbenke/repo/recSys/database/data:/data \
	--env NEO4J_AUTH=neo4j/test \
	--name database_docker database_img
