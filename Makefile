init:
	pip install -r requirements.txt

test:
	pytest tests --cov-config .coveragerc --cov=esperanto_analyzer --cov-report=html

lint:
	pylint esperanto_analyzer/ --reports=n -f json > .lint_results