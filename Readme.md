### To run this project

* First install all python package in requirements.txt
* Run makemigrations then migrate all
* Create a superuser ``` python manage.py createsuperuser ``` then follow the steps
* Open two terminal
  * First one: you run django-tailwind with ``` python manage.py tailwind start ```
  * Second one : you run django runserver ``` python manage.py runserver ```
* You can go to /admin to use django-admin panel

### Run this project with docker
* Make sure you have docker & docker-compose install
* Then run ``` docker-compose up ```
 * If it doesn't work -> run first ``` docker-compose build ``` then ``` docker-compose-up ```