#!/bin/bash

sudo docker stop ptt_auto_login
sudo echo y|sudo docker system prune
sudo docker build -t ptt_auto_login .
sudo docker run --restart always --env-file .env --name ptt_auto_login -d ptt_auto_login
