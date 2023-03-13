install:
	poetry install

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-prog:
	poetry run brain-prog

build:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make-lint:
	poetry run flake8 brain_games

