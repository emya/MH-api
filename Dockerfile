FROM python:3.6

ENV POSTGRES_HOST=myNetwork\
    POSTGRES_PASSWORD=postgres

RUN mkdir -p /opt
WORKDIR /opt


RUN set -ex; \
    pip install --upgrade pip;

ADD . /opt

RUN pip install -r requirements.txt

EXPOSE 5432

CMD ["python", "-u", "/opt/app.py"]