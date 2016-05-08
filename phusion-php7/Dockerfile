FROM phusion/baseimage:0.9.18

# Environment variables
ENV DEBIAN_FRONTEND noninteractive

# Initialize phusion/baseimage
CMD ["/sbin/my_init"]

# Add PHP 7 repo
RUN apt-get install -y --force-yes language-pack-en-base
RUN add-apt-repository -y ppa:ondrej/php

# Update package cache
RUN apt-get update

# Install PHP 7, nginx
RUN apt-get install -y --force-yes php7.0
RUN apt-get install -y --force-yes php7.0-mcrypt php7.0-mbstring php7.0-zip php7.0-xml php7.0-curl
RUN apt-get install -y --force-yes php7.0-mysql
RUN phpdismod mysqli

RUN apt-get install -y --force-yes nginx

RUN apt-get install -y --force-yes php7.0-dev
RUN apt-get install -y --force-yes libhiredis-dev
WORKDIR /tmp
RUN apt-get install -y --force-yes git
RUN git clone https://github.com/Danack/phpiredis.git
WORKDIR /tmp/phpiredis
RUN phpize
RUN ./configure --enable-phpiredis
RUN make
RUN make install
RUN echo "extension=phpiredis.so" > /etc/php/7.0/mods-available/phpiredis.ini
RUN phpenmod phpiredis

# Copy configuration
COPY ./phusion-php7/nginx.conf /etc/nginx/
COPY ./phusion-php7/php-fpm.conf /etc/php/7.0/fpm/

# Copy services
COPY ./phusion-php7/php-fpm.sh /etc/service/php-fpm/run
COPY ./phusion-php7/nginx.sh /etc/service/nginx/run

# Add files
ADD ./src/ /var/www/

# Set workdir to /var/www so that docker exec starts here
WORKDIR /var/www/

# Cleanup
RUN apt-get clean -y --force-yes && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# nginx listens on the following port, so expose it
EXPOSE 80
