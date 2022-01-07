SUBJECT_FILES=siphotonics/*.py tests/*.py setup.py

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format:
	autoflake --in-place --remove-all-unused-imports \
		--remove-unused-variables --expand-star-imports \
		--ignore-init-module-imports $(SUBJECT_FILES) && \
	isort --filter-files $(SUBJECT_FILES) && \
	black --line-length=120 $(SUBJECT_FILES)

lint:
	pylint --disable=R,C,W1514 \
 		$(SUBJECT_FILES)

test:
	python -m pytest -vv --cov=siphotonics

all: install lint test

ci:
	pre-commit lint test