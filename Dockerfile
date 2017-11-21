FROM ubuntu:17.10

MAINTAINER Pablo Molina Gómez

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/pmolinag/proyecto.git
RUN cd proyecto/ && pip3 install -r requirements.txt

EXPOSE 8000
WORKDIR proyecto/
CMD gunicorn app:app --log-file=- --bind 0.0.0.0:8000
