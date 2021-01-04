clean:
	rm -rf build
	rm -rf dist
	rm -rf ziproto.egg-info
build:
	python3 setup.py build
	python3 setup.py sdist
install:
	python3 setup.py install
publish:
	python3 -m pip install wheel
	python3 -m pip install twine
	make clean
	python3 setup.py bdist_wheel
	python3 -m twine upload dist/*
