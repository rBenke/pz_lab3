docker run --rm -it \
	--network recnet \
	-v /home/rbenke/repo/recSys/search_engine/app:/app \
	--name search_engine_docker search_engine_img
