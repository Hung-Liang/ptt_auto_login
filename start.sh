#!/bin/bash

sudo docker stop ptt_auto_login
echo y|docker system prune
sudo docker build --no-cache -t ptt_auto_login .
sudo docker run --restart always --name ptt_auto_login -d ptt_auto_login
