# Install docker
sudo apt-get update
sudo apt install docker.io

Avoid typing sudo for docker:
sudo usermod -aG docker $(whoami)

docker info

# Show running docker processes (-a: show all, active and inactive)
docker ps -a

# List docker networks
docker network ls

# Show docker images
docker images

# Remove docker image (-f: remove regardless of the image being used)
docker rmi -f <IMAGE_ID>

# Remove docker image labelled with a tag
docker rmi <IMAGE_ID>:<TAG>

# Remove docker container (-f: remove regardless of the container is running)
docker rm -f <CONTAINER_ID>

# Start a new instance (container) from a docker image (-d: detached, run container in background, -p: publish / port forwarding)
# TAG_NAME is necessary, if there is no latest (default)
docker run -d -p <HOST_PORT>:<CONTAINER_PORT> <DOCKER_IMAGME_NAME>:<TAG_NAME>

# Run a command in docker container (-i: interactive, STDIN is open even when container is not attached, -t: terminal)
docker exec -ti <CONTAINER_NAME>

# Open bash to container in interactive mode
docker exec -ti <CONTAINER_NAME> bash

# Stop docker container
docker stop <CONTAINER_ID>

Build a docker image from a Dockerfile:
1. create a Dockerfile (using this name)
vim Dockerfile:

FROM php:7.2-apache
EXPOSE 80
COPY index.php /var/www/html/index.php


# Build docker image using Dockerfile
docker build -t test .

# Export docker image
docker save -o <path for generated tar file> <IMAGE_NAME>

# Import generated docker image
docker load -i <path to image tar file>

# Get info about container:
docker inspect <CONTAINER_ID>

# RabbitMQ in docker:
docker run -d --hostname jager-rabbit-host --name jager-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3

# Check memory and CPU usage of container:
docker stats <CONTAINER_ID>

# Tag an image (creates a new image):
docker tag <IMAGE_ID> <REPOSITORY_NAME>:<TAG>

# If something missing in the docker image, build again
docker build --tag reactor-1.1 .

# Run docker container
docker run --publish 1986:1986 reactor-1.1:latest

# In the other terminal, take curl requests:
curl http://localhost:1986/api/checktemperature

curl http://localhost:1986/api/reactor_status

curl http://localhost:1986/

curl http://localhost:1986/api/controlrods
