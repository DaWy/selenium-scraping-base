FROM python:latest
RUN apt update

# Base Dependencies
RUN apt install -y xvfb git

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y -f

# Python Packages
RUN pip install pyvirtualdisplay selenium

# Main APP
RUN mkdir /app
RUN git clone https://github.com/DaWy/selenium-scraping-base.git /app

# Adding APP directory to the PATH
RUN echo "PATH=$PATH:/app" >> /root/.bashrc

