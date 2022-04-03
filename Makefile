.PHONY: run-dev
run-dev:
	FLASK_APP=server.py flask run

.PHONY: format
format:
	python -m black app/ ; python -m black server.py

.PHONY: format-check
format-check:
	python -m black app/ --check ; python -m black server.py --check