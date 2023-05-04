migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

check:
	flake8 .
	isort .