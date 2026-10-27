#!/bin/bash

sudo docker stop ptt_auto_login
sudo echo y|sudo docker system prune
sudo docker build -t ptt_auto_login .
sudo docker run --restart always -v "$(pwd)/.env:/ptt_auto_login/.env:ro" --name ptt_auto_login -d ptt_auto_login
