FROM python/3-bullseye

MAINTAINER Guy Or

# Create app directory
WORKDIR /usr/src/app

# Copy source and config files
COPY . ./

# Install dependencies and set virtual env for python
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update && apt-get install -y gosu && python3 -m venv $VIRTUAL_ENV && pip install -r requirements.txt

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["run-app"]
