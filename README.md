Coding-challange
--------------

Assignment topic here [assignment](./assignment.md)


## Setup and Installation

You would required Docker and Docker-compose in order to build this project on your local machine.

```sh
docker-compose build web
docker-compose run web python manage.py migrate # run the migrations
docker-compose run web python manage.py createsuperuser # to create the superuser
```


## Running the project

In order to run the project `docker-compose up` will run the project and you can browse the running project at http://localhost:8000

