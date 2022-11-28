docker run --rm -it \
       --name client_img \
       --network recnet \
       -v $(pwd)/../app:/app \
       client_img
