docker run --rm -it \
	--network recnet \
	-v /home/rbenke/repo/recSys/model/app:/app \
	--name model_docker model_img
