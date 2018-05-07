.PHONY: run

run:
	docker-compose up

run-debug:
	docker-compose run --services-ports pythonrio

migrate:
	docker-compose exec pythonrio python3 manage.py migrate

