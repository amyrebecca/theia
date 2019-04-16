FROM python:3

LABEL maintainer="contact@zooniverse.org"

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    postgresql-client \
    gdal-bin \
    libgdal-dev \
    python-gdal \
    python3-gdal \
    binutils \
    netcat \
    libproj-dev \
    libgeoip1 \
    postgis \
  && rm -rf /var/lib/apt/lists/*

RUN pip install \
  pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --system --dev

RUN export GDAL_VERSION=$(gdal-config --version) \
  && pip install --global-option=build_ext --global-option="-I/usr/include/gdal/" \
    gdal~=${GDAL_VERSION}

ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["bash", "start_server.sh"]