FROM python:3.6.4-alpine3.7

# Prepare environment
RUN apk add --update git make gcc g++ python3-dev musl-dev postgresql-dev libuv-dev libffi-dev jpeg-dev zlib-dev

# Move to WORKDIR and copy files
WORKDIR /usr/src/app
ADD . .

# Install dependencies
RUN set -ex && \
    pip install honcho && \
    pip install -r requirements.txt

CMD ["honcho", "start"]