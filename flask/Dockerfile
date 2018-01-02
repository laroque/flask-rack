from python:3.4

COPY hipflask /usr/local/src/hipflask
COPY setup.py /usr/local/src/setup.py

RUN pip install -e /usr/local/src

RUN pip install uwsgi

COPY hipflask_uwsgi.yaml /usr/local/etc/hipflask_uwsgi.yaml

CMD ["/usr/local/bin/uwsgi", "--yaml", "/usr/local/etc/hipflask_uwsgi.yaml"]
