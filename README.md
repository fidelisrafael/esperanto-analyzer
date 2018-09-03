# Esperanto Analyzer

----

### Build Status:

#### Development:

[![Build Status](https://travis-ci.com/fidelisrafael/esperanto-analyzer.svg?token=k5uMpn3U564QqWar8oA1&branch=development)](https://travis-ci.com/fidelisrafael/esperanto-analyzer)

#### Master:

[![Build Status](https://travis-ci.com/fidelisrafael/esperanto-analyzer.svg?token=k5uMpn3U564QqWar8oA1&branch=master)](https://travis-ci.com/fidelisrafael/esperanto-analyzer)

---

### About

This projects aim to create one Esperanto analyzer for Ruby Language.


### Development

Clone this repository:

```
git clone https://github.com/fidelisrafael/esperanto-analyzer.git
cd esperanto-analyzer
```

Make sure you have `virtualenv` >= `16.0.0` installed:

```
$ virtualenv --help
16.0.0
```

Otherwise, [install it](https://virtualenv.pypa.io/en/stable/installation/).

Then, creates one new env and activate it:

```
$ virtualenv env
$ source env/bin/activate
```

Install the dependencies for development and test enviroments:

```
# If you just want to install the needed dependencies for production, just run: `make init`
$ make init_dev
```

Run the tests:

```
$ make test
```

You can follow the code coverage stats opening: `coverage/index.html`


#### Web API

This library cames with a very simple HTTP Server built on top of Flask to provide
an WEB API interface for integration with others systems. You can run the HTTP server
running the following make task:

```
$ make web_api # or simply running: python web/runserver.py
```

This server has auto-reload(or hot-reload) enabled by default, so you don't need to restart
the server when you change the source code.

To test it:

```
curl http://127.0.0.1:5000/analyze?sentence=Kio%20estas%20Esperanto%3F%20%C4%9Ci%20estas%20lingvo%20tre%20ta%C5%ADga%20por%20internacia%20komunikado.
```
