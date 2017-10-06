venv:
	virtualenv venv/
	venv/bin/python setup.py develop

clean:
	rm -rf *.pyc loofah.egg-info
