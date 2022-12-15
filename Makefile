build:
	python3 -m venv env
	. ./env/bin/activate
	pip install -r requirements.txt

build_dev: build
	pip install -r requirements.dev.txt

run:
	uvicorn app.bin.app:app --reload

run_prod:
	uvicorn app.bin.app:app

test:
	tox
	coverage html

load_test:
	locust
