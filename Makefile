ACTIVATE_VENV := venv/bin/activate
ACTIVATE_VENV := venv/bin/activate

# Create virtualenv if none exists.
.PHONY: create-venv
create-venv:
	test -d venv || python3 -m virtualenv venv

.PHONY: install-deps
install-deps: create-venv
	. $(ACTIVATE_VENV) && pip install -r requirements.txt

.PHONY: run
run:
	docker-compose -f docker-compose.yml up --build -d

.PHONY: stop
stop:
	docker-compose -f docker-compose.yml stop

.PHONY: run-dev
run-dev:
	. $(ACTIVATE_VENV) && FLASK_APP=server.py flask run

.PHONY: format
format:
	. $(ACTIVATE_VENV) && python -m black .

.PHONY: format-check
format-check:
	. $(ACTIVATE_VENV) && python -m black . --check

.PHONY: run-tests
run-tests: unit-test int-test

.PHONY: unit-test
unit-test:
	. $(ACTIVATE_VENV) && python -m unittest discover tests/unit

.PHONY: int-test
int-test: 
	. $(ACTIVATE_VENV)  && python -m unittest discover tests/integration
