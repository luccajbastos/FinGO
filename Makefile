
PORT=8000

# Iniciar
start:
	python3 manage.py flush --no-input
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver 0.0.0.0:${PORT}

start-db:
	docker run -d \
	--name fingodev-postgres \
	-e POSTGRES_USER=root \
	-e POSTGRES_PASSWORD=dev \
	-e POSTGRES_DB=fingodev \
	-p 5432:5432 \
	postgres:15-alpine
