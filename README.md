# theia
Planning the next-generation Floating Forests pipeline

## Etymology

Theia is the Greek goddess of sight and of the blue sky. She is the mother of the sun, the moon, and the dawn. Our hope is to use Theia to acquire satellite images and find blue skies!

## Tech

The proposed tech stack for Theia is:

* Django / GeoDjango
* Django REST Framework
* Requests / Requests OAuth
* Postgres
* Celery
* gdal
* Pillow
* Docker / Kubernetes

## Getting started

### Docker environment

#### Build Image

Ensure that you have a modern-ish version of docker installed. Simply run

`docker build -t theia .` to build the image

If you have an image built, you can run it with:

`docker run theia`

#### Build Environment

To create the environment, including the postgres and redis servers and a web app and worker node

`docker-compose up &`

To, for example, create a second worker node

`docker-compose up --scale worker=2 &`

To halt instances

`docker-compose down`

Note that you can also remove the volumes (they will need to be recreated next time)

`docker-compose down -v`

### Local environment

Make sure that you have an entry in your `/etc/hosts` file that looks like this:

`127.0.0.1  postgres`

so that we can find the postgres server when the app is running locally

Install the correct version of postgres:

`brew install postgresql@9.4`

If you already had a postgres install, you should be able to select your postgres version this way:

`brew switch postgresql 9.4`

If not, you can also use this keg-only formula by force-linking it:

`brew link postgresql@9.4 --force`

Add the user `theia` with password `theia`:

`createuser theia -d -P`

Make sure that you have an entry in your `/etc/hosts` file that looks like this:

`127.0.0.1 redis`

so that we can find the redis server when the app is running locally

Install the current version of redis:

`brew install redis`

Ensure that you have a modern python:

`brew install python`

and follow the installation notes to put the versionless alias on your `$PATH`.

Then install `pipenv` package and virtual environment manager

`pip install pipenv`

Then use `pipenv` to install dependencies:

`pipenv install --dev`

Install GIS related dependencies:

`brew install postgis gdal`

Install other related dependencies:

`brew install libtiff`

To drop or create the local DB that theia will be using:

`pipenv run create_local_db`

`pipenv run drop_local_db`

Run Django app locally (applying migrations if necessary):

`pipenv run server`

Run the Celery worker locally (does not apply migrations):

`pipenv run worker`

### Accessing the app

Regardless of whether you're running it locally or inside the image, the Django app can be accessed at http://localhost:8080/

### Running the tests

Locally:

Make sure that you have done all of the above, and if you have never run the server you may also need to run the migrations:

`pipenv run migrate`

and then you can run the tests with

`pipenv run tests`

In the container:

`docker-compose up postgres && docker-compose run app bash -c 'python -B -m pytest'`
