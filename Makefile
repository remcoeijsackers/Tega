.PHONY: build
build:
	docker build . -t tega-app

.PHONY: up
up: build
	docker run --rm -p 9000:9000 tega-app 

.PHONY: stop
stop:
	docker stop $(shell docker ps -q --filter ancestor=tega-app)

.PHONY: clean
clean: stop
	docker rm $(shell docker ps -a -q --filter ancestor=tega-app)


test-flake8: 
	docker run --rm tega-app python -m flake8 /code

test-python:
	docker run --rm tega-app python -m unittest discover -s tests

.PHONY: test
test: build test-python test-flake8