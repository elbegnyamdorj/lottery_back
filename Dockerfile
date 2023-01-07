##--platform=linux/amd64

FROM python:3.10.6-alpine 
ENV PATH="/scripts:${PATH}"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache python3 postgresql-libs 
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev 
RUN python -m pip install --upgrade pip
RUN apk add jpeg-dev zlib-dev libjpeg
RUN pip install -r /requirements.txt
RUN apk del .build-deps
RUN apk del .tmp

RUN mkdir -p /app
COPY ./app /app

WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/* 


RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

CMD ["entrypoint.sh"]