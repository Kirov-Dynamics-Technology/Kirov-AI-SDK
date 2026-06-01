.PHONY: install run test lint example clean

install:
	pip install -r requirements.txt

run:
	uvicorn app:app --reload --port 8000

test:
	pytest -v

example:
	python example.py

lint:
	ruff check kirov_ai/ tests/ app.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
