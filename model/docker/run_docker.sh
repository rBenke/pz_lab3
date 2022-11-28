docker run --rm -it \
	--network recnet \
	-v $(pwd)/../app:/app \
	--name model_docker model_img
