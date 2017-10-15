from nginx:1.13.5

# For now these are all volume mounted in docker-compose, but I also add them
# here so that you can build the container directly and expect it to work in
# the same way.
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx_conf.d /etc/nginx/conf.d

# create an ssl certificate
RUN apt-get update && apt-get install -y ssl-cert
RUN make-ssl-cert generate-default-snakeoil --force-overwrite
