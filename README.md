To start a container in Docker, we first create a folder with the Dockerfile, where we define the base image and the container configuration. 
Outside this folder, we create a docker-compose.yml file. In this file, we configure the services and the port we want to expose. 
From the terminal, we run `docker-compose up -d`, and then we access localhost where our container is already up and running.
