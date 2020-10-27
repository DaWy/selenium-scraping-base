FROM python:latest

RUN apt update
# Base Dependencies
RUN apt install -y xvfb git
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y -f

RUN pip install pyvirtualdisplay selenium

RUN mkdir /app
RUN git clone https://github.com/DaWy/selenium-scraping-base.git /app

RUN echo "PATH=$PATH:/app" >> /root/.bashrc


RUN apt install nano -y
