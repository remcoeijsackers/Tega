VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
FLAGS = flags


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run2: $(VENV)/bin/activate
	$(PYTHON) tega.py account

clean2:
	rm -rf __pycache__
	rm -rf $(VENV)

up2: 
	python3 -m tega.py account

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
environment = local

# Define default target
.PHONY: all
all: build run

# Build Docker image
.PHONY: build
build:
	docker build docker/environment/$(environment) -t tega-app

# Run Docker container
.PHONY: run
run: build
	docker run -p 9000:9000 tega-app

# Stop Docker container
.PHONY: stop
stop:
	docker stop $(shell docker ps -q --filter ancestor=tega-app)

# Remove Docker container
.PHONY: clean
clean: stop
	docker rm $(shell docker ps -a -q --filter ancestor=tega-app)

.PHONY: test
test: 
	docker run -p 9000:9000 tega-app