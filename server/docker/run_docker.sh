docker run --rm -it \
	--network recnet \
	-v /home/rbenke/repo/recSys/server/app:/app \
	--name server_img server_img
