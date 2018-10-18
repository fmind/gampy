.PHONY: cover

NAME = $(shell .venv/bin/python setup.py --name)

init-covers: .venv
	.venv/bin/pip install '.[covers]'

clean-covers:
	find . -name '.mypy_cache' -exec rm -fr {} +

commit-covers: report;

cover: .venv
	.venv/bin/coverage run --rcfile="covers/coverage.ini" --source ${NAME} -m pytest -q

report: .venv cover
	.venv/bin/coverage report --rcfile="covers/coverage.ini"

htmlcov: .venv cover
	.venv/bin/coverage html --rcfile="covers/coverage.ini" --directory="covers/htmlcov"
