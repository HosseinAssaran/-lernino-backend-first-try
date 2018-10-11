FROM debian:stretch-slim

MAINTAINER Salar Moghaddam

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get install -y \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	libmariadbclient-dev && \
        rm -rf /var/lib/apt/lists/* && \
	pip3 install uwsgi && \
	mkdir -p /var/www

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

COPY requirements.txt /var/www
RUN pip3 install -r /var/www/requirements.txt

# add (the rest of) our code
COPY . /var/www

WORKDIR /var/www

RUN chmod +x entrypoint.sh

EXPOSE 80

#RUN cd /var/www/ && python3 manage.py collectstatics
CMD ["/var/www/entrypoint.sh"]
