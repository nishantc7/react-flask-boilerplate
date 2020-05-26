FROM python:3.6.4
# Dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends netcat \
    && apt-get -q clean

# set working directory 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint-prod.sh /usr/src/app/entrypoint-prod.sh
COPY . /usr/src/app
CMD ["./entrypoint-prod.sh"]