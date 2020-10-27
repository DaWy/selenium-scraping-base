USE python:latest

RUN apt update
RUN apt install -y xvfb

RUN echo "PATH=$PATH:/app" >> /root/.bashrc


RUN apt install nano -y
