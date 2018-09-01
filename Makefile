init:
	pip install -r requirements.txt

test:
	pytest tests -v --cov-config .coveragerc --cov=esperanto_analyzer --cov-report=html

lint:
	pylint esperanto_analyzer/ --reports=n -f json > .lint_results

formatted_lint:
	pylint esperanto_analyzer/ --reports=n -f json | pylint-json2html -o pylint.html

web_api:
	python web/runserver.py
