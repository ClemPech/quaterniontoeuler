PACKAGE_NAME = quat2eul
SRC = $(PACKAGE_NAME) tests setup.py

all: test


.install-deps: $(shell find requirements -type f)
	@pip3 install -U -r requirements/dev.txt
	@touch .install-deps

.develop: .install-deps $(shell find $(PACKAGE_NAME) -type f)
	@pip3 install -e .
	@touch .develop

pylint:
	pylint --disable=C0114,C0115,C0116,W0212,W0122,W0621 --good-names=q0,q1,q2,q3 $(SRC)

black-check:
	black --check --diff -t py35 $(SRC)

lint: pylint black-check

fmt:
	black -t py35 $(SRC)


test: lint .develop
	pytest ./tests ./$(PACKAGE_NAME)


vtest: lint .develop
	pytest ./tests ./$(PACKAGE_NAME) -v


cov: lint .develop
	pytest --cov $(PACKAGE_NAME) --cov-report html --cov-report term ./tests/ ./$(PACKAGE_NAME)/
	@echo "open file://`pwd`/htmlcov/index.html"


doc: doctest doc-spelling
	make -C docs html SPHINXOPTS="-W -E"
	@echo "open file://`pwd`/docs/_build/html/index.html"


doctest: .develop
	make -C docs doctest SPHINXOPTS="-W -E"


doc-spelling:
	make -C docs spelling SPHINXOPTS="-W -E"

readmeMD:
	sphinx-build -M markdown ./docs/source/ ./docs/source/_build 
	rm -f README.md
	mv ./docs/source/_build/markdown/index.md README.md