TARGET_FILES=sipkit/*.py tests/*.py setup.py

install:
	pip install --upgrade pip && \
		pip install -e .[dev]

format:
	autoflake --in-place --remove-all-unused-imports \
		--remove-unused-variables --expand-star-imports \
		--ignore-init-module-imports \
			$(TARGET_FILES) && \
	isort --filter-files $(TARGET_FILES) && \
	black --line-length=120 $(TARGET_FILES)

lint:
	- pylint --disable=R0911,R0912,C0114,W1514 \
		--max-line-length=120  --exit-zero --output-format=text \
			$(TARGET_FILES)
test:
	python -m pytest -vv --cov=sipkit --disable-warnings

ci: install lint test

all: install format lint test
