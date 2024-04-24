run-install:
	poetry install
	poetry shell

run : 
	poetry shell
	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations
	python manage.py runserver

install-run-docker :
	docker-compose build
	docker-compose up

run-docker :
	docker-compose up
