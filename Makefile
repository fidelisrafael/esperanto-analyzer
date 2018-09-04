init:
	pip install -r requirements.txt

init_dev:
	pip install -r development_requirements.txt
	pip install -r test_requirements.txt
	pip install -r requirements.txt

test:
	pytest tests --cov-config .coveragerc --cov=esperanto_analyzer --cov-report=html

lint:
	pylint esperanto_analyzer/ --reports=n -f json > .lint_results

formatted_lint:
	pylint esperanto_analyzer/ --reports=n -f json | pylint-json2html -o pylint.html

web_api:
	python esperanto_analyzer/web/runserver.py
