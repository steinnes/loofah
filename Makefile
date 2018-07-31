venv:
	virtualenv venv/
	venv/bin/python setup.py develop

clean:
	rm -rf *.pyc loofah.egg-info

release:
	@-rm dist/*
	venv/bin/python setup.py sdist bdist_wheel
	@read -n 1 -r -p "Release to PyPI? " REPLY; \
	if [ "$$REPLY" == "y" ]; then\
		twine upload dist/*.tar.gz;\
		twine upload dist/*.whl;\
	else\
		echo "Not uploading..";\
	fi
