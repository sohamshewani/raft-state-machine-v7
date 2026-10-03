all:
	python3 -m venv venv
	. venv/bin/activate

test:
	python3 -m unittest tests/test_runner
	
install:
	pip install -r requirements.txt
	
build:
	python3 setup.py sdist bdist_wheel
