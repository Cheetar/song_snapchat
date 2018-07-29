FROM ubuntu:16.04

ENV PYTHONUNBUFFERED 1

USER root

RUN apt-get update

RUN apt-get --assume-yes install software-properties-common
RUN add-apt-repository ppa:mc3man/xerus-media
RUN apt-get update
RUN apt-get --assume-yes install ffmpeg
RUN apt-get --assume-yes install frei0r-plugins

RUN apt-get --assume-yes install python3-pip

RUN mkdir /code
ADD . /code

RUN pip3 install -r /code/app/requirements.txt
