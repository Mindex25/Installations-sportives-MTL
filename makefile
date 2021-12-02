export FLASK_APP=index.py

run:
	raml2html doc.raml > app/templates/doc.html
	python3 wsgi.py