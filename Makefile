all: init test

init:
	python setup.py develop
	pip install tox coverage

test:
	coverage erase
	detox
	coverage html
