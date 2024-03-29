install:
	pip install --upgrade pip  &&\
		pip install -r requirements.txt

test:
	python -m pytest --cov=exceptions --cov=footballer tests

format:
	black *.py

lint:
	pylint --disable=R,C main.py

all: install lint test format