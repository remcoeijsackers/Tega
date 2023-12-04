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
