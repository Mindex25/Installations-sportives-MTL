export FLASK_APP=index.py
export FLASK_ENV=development

run:
	raml2html doc.raml > app/templates/doc.html
	python3 wsgi.py