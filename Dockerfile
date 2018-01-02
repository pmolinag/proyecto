FROM ubuntu:17.10

MAINTAINER Pablo Molina Gómez

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN git clone https://github.com/pmolinag/proyecto.git
RUN cd proyecto/ && pip install -r requirements.txt


EXPOSE 8000
WORKDIR proyecto/FlyFinderBot/
CMD gunicorn vuelos_rest:app --log-file - --bind 0.0.0.0:8000
