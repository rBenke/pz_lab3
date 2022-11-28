docker run --rm -it \
	--network recnet \
	-v $(pwd)/../app:/app \
	--name server_img server_img
