docker run --rm -it \
	--network recnet \
	-v $(pwd)/../app:/app \
	--name search_engine_docker search_engine_img
