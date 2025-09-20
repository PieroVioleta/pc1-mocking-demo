run:
	poetry run uvicorn app.main:app --reload

test:
	poetry run pytest -q
