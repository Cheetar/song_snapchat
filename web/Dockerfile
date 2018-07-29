FROM ubuntu:16.04

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
RUN pip3 install -r /code/app/requirements.txt

RUN sudo add-apt-repository ppa:mc3man/trusty-media
RUN sudo apt-get update
RUN sudo apt-get install ffmpeg
RUN sudo apt-get install frei0r-plugins  
