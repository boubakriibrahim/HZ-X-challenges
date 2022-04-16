#!/bin/bash
docker rm -f soolmate
docker build -t soolmate . && \
docker run --name=soolmate --rm -p1337:80 -it soolmate
