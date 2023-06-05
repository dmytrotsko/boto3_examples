#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world

