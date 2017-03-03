.PHONY: all
all: install

.PHONY: setup
setup:
	pip install pipenv

.PHONY: install
install:
	pipenv run pip install -r requirements.txt

.PHONY: run
run: install
	pipenv shell -c "heroku local; exit $$?"
