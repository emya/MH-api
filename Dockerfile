FROM python:3.6

ENV POSTGRES_HOST=localhost\
    POSTGRES_PASSWORD=password

RUN mkdir -p /opt
WORKDIR /opt

RUN set -ex;
    pip install --upgrade pip;

ADD . /opt

RUN pip install -r requirements.txt

CMD ["python", "-u", "/opt/app.py"]