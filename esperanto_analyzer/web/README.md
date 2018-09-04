Esperanto Analyzer WEB API
=================

Usage
-----

Clone the repo:
    (...)

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py develop # or install if you prefer

Run the sample server

    python runserver.py

Try the endpoints:

    curl -XGET http://localhost:5000/analyze?sentence=Mia%20nomo%20estas%20Rafaelo%20kaj%20mi%20venas%20el%20Brazilo


Swagger docs available at `http://localhost:5000/api/spec.html`


License
-------

MIT, see LICENSE file

