docker run --rm -it \
       --name client_img \
       --network recnet \
       -v /home/rbenke/repo/recSys/client/app:/app \
       client_img
