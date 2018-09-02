init:
	pip install -r requirements.txt

test:
	pytest tests --cov-config .coveragerc --cov=esperanto_analyzer --cov-report=html

lint:
	pylint esperanto_analyzer/ --reports=n -f json > .lint_results
	pylint web/ --reports=n -f json > .web_lint_results

formatted_lint:
	pylint esperanto_analyzer/ --reports=n -f json | pylint-json2html -o pylint.html
	pylint web/ --reports=n -f json | pylint-json2html -o pylint_web.html

web_api:
	python web/runserver.py
