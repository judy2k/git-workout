all: help

install:
	pip install --upgrade pip-tools
	pip-sync requirements.txt dev-requirements.txt
	pip install -e .

help:
	echo "requirements - Update requirements.txt when setup.py changes"

requirements: requirements.txt dev-requirements.txt

requirements.txt: setup.py
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --generate-hashes

dev-requirements.txt: dev-requirements.in
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile dev-requirements.in --generate-hashes

upgrade:
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --generate-hashes --upgrade
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile dev-requirements.in --generate-hashes --upgrade

package:
	pip wheel --wheel-dir dist --no-deps .
	python setup.py sdist

clean:
	rm -rf build dist

.PHONY: all clean help install package requirements upgrade
