.PHONY: run test build publish clean

run:
	python3 -m grepy.cli -rn result .

test:
	python3 -m unittest tests/*py

install:
	pip3 install .

build:
	python3 setup.py sdist bdist_wheel

publish: build
	twine upload dist/*

clean:
	rm -rf dist build lr_grepy.egg-info
