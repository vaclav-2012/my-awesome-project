SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	mypy my_awesome_project tests/test_example
	flake8 .
	doc8 -q docs

.PHONY: unit
unit:
	pytest

.PHONY: package
package:
	poetry check
	pip check
	safety check --bare --full-report --ignore=38330

.PHONY: test
test: lint unit package
