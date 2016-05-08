#!/bin/sh
exec /usr/sbin/php-fpm7.0 >>/var/log/php-fpm.log 2>&1
