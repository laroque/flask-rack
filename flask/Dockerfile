from python:3.4

COPY hipflask /usr/local/src/hipflask
COPY setup.py /usr/local/src/setup.py

RUN pip install -e /usr/local/src

ENV FLASK_APP hipflask
ENV FLASK_DEBUG true

CMD ["flask","run","--host=0.0.0.0"]
