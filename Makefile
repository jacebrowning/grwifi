.PHONY: all
all: build

.PHONY: install
install:
	poetry install

.PHONY: build
build: install
	poetry run python format.py map.geojson

.PHONY: run
run: build
	poetry run sappy
