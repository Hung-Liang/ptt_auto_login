#!/bin/bash

# Rebuild only changed layers and recreate the container when image or config changed
sudo docker compose up -d --build
