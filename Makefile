.PHONY: run-dev
run-dev:
	FLASK_APP=server.py flask run

.PHONY: format
format:
	black app/ black server.py

.PHONY: format-check
format-check:
	python -m black app/ --check ; python -m black server.py --check