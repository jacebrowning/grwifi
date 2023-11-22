PORT ?= 5000

.PHONY: all
all: build

.PHONY: install
install:
	poetry install --no-root

.PHONY: build
build: install
	- mv ~/Downloads/map.geojson .
	poetry run python format.py map.geojson

.PHONY: run
run: build
	poetry run sappy --port=$(PORT)

.PHONY: clean
clean:
	rm -rf .venv
