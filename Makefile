ACTIVATE_VENV := venv/bin/activate
ACTIVATE_VENV := venv/bin/activate

# Create virtualenv if none exists.
.PHONY: create-venv
create-venv:
	test -d venv || python3 -m virtualenv venv

.PHONY: install-deps
install-deps: create-venv
	. $(ACTIVATE_VENV) && pip install -r requirements.txt

.PHONY: run-dev
run-dev:
	. $(ACTIVATE_VENV) && FLASK_APP=server.py flask run

.PHONY: format
format:
	. $(ACTIVATE_VENV) && python -m black app/ ; . $(ACTIVATE_VENV) && python -m black server.py

.PHONY: format-check
format-check:
	. $(ACTIVATE_VENV) && python -m black app/ --check ; . $(ACTIVATE_VENV) && python -m black server.py --check