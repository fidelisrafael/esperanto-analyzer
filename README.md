# Esperanto Analyzer

----

![Esperanto Flag](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Flag_of_Esperanto.svg/640px-Flag_of_Esperanto.svg.png?1535986891157)

## Build Status:

### Development:

[![Build Status](https://travis-ci.com/fidelisrafael/esperanto-analyzer.svg?token=k5uMpn3U564QqWar8oA1&branch=development)](https://travis-ci.com/fidelisrafael/esperanto-analyzer)

### Master:

[![Build Status](https://travis-ci.com/fidelisrafael/esperanto-analyzer.svg?token=k5uMpn3U564QqWar8oA1&branch=master)](https://travis-ci.com/fidelisrafael/esperanto-analyzer)

---

### Atendu! Kio estas Esperanto? (_Wait! What is Esperanto?_)

That is a fair question! Esperanto is the most widely spoken  constructed international auxiliary language
(_conlang_) in the world. It was created back in **1887** by a polish-jewish guy named "Ludwik Lejzer Zamenhof"_(often refered as L.L Zamenhof)_.  Zamenhof's goal was to **create an easy and flexible language** that would serve as a universal second language to foster peace and international understanding of people from all around the world.

The phonology, grammar, vocabulary, and semantics are based on the **Indo-European**(_Italian_,_Spanish_,_French_, _Catalan_, _Russian_, _German_...) languages spoken in Europe. The sound inventory is essentially **Slavic**, as is much of the semantics, whereas the vocabulary derives primarily from the **Romance languages**, with a lesser contribution from **Germanic languages** and minor contributions from **Slavic languages** and **Greek**.

The language has more than **130 years of history** and culture now, and a very active community  as well.

Esperanto is a SUPER  regular language, this means that the language does not have **irregular verbs** or **gender distinction for articles**, beside this Esperanto has only **16 grammar rules**.
For example, one of the rules:  ALL **Nouns** MUST end with the vowel `o`, eg:

- `domo`
- `homo`
- `komputilo`
- `komputilisto`

Or  **Adjectives** MUST end with the letter `a`, eg:

- `bela`
- `granda`
- `varma`
- `malvarma`

If you want to know (or learn) more about Esperanto, you should read the following links:

 - [Esperanto at Wikipedia](https://www.wikiwand.com/en/Esperanto)
 - [Kio estas Esperanto? (in Esperanto)](https://lernu.net/eo/esperanto) or in [English](https://lernu.net/es/esperanto)
- Esperanto course at Duolingo for: [[English speakers]](https://www.duolingo.com/course/eo/en/Learn-Esperanto-Online), [[Portuguese speakers]](https://www.duolingo.com/course/eo/pt/Learn-Esperanto-Online), [[Spanish speakers]](https://www.duolingo.com/course/eo/es/Learn-Esperanto-Online)
 - [Esperanto course at Lernu.net](http://lernu.net/kurso)
 - [Youtube serie: Esperanto estas...](https://www.youtube.com/watch?v=RlftmTm8I18&list=PL83728C14BFC5822F)

---

## About this project

The aim of this project is to create one tool that can read and grammarly classify Esperanto sentences.

The first part of project consists in **Morphological Analyzes** of Esperanto words, the next step is to create a **Syntactical Analyzer** for the language as well.

---

## How to use it?

Simple! You can use it from the CLI(_Command Line Interface_) or importing as a library within your Python code.

Let's start using the CLI to morphologically classify one basic Esperanto sentence:

## Installation

First, install it:

```bash
$ pip install esperanto-analyzer
```

Now you will have the libraries source-code files in your system, and also the executable `binary` through CLI, test it:

```bash
$ eo-analyzer --version
> Version: 0.0.1
```

## CLI usage:

```sh
$ eo-analyzer "Jen la alfabeto de Esperanto. Ĉiu litero ĉiam sonas same kaj literumado estas perfekte regula. Klaku la ekzemplojn por aŭdi la elparolon!"
```

![eo-analyzer response](https://i.imgur.com/4hWUcWY.png)

Pretty cool humn?

## Python library usage

Ok, so now you want to import this library in your project, right? That's super simple, just drop these lines in your project:

### Morphological analyzes of sentences

```py
from esperanto_analyzer import MorphologicalSentenceAnalyzer

# Creates one instance to morphologically analyzes one sentence
analyzer = MorphologicalSentenceAnalyzer("Esperanto estas tre facila lingvo al lerni.")
analyzer.analyze() # => Returns True/False

# This is the simplest human-readable response of the morphological analyzes' results
print(analyzer.simple_results())
# => [['Esperanto', 'Noun'], ['estas', 'Verb'], ['tre', 'Adverb'], ['facila', 'Adjective'], ['lingvo', 'Noun'], ['al', 'Preposition'], ['lerni', 'Verb']]

```

But you can always deal with a more complex results set if you (or better, your software) want/need to:

```py
# The `#results()` method returns a Array object wirh a more complex structure than `#simple_results()` method
results = analyzer.analyzes_results()
first_analyze = results[0]

# Returns and Array object with `AnalyzeResult` objects
print(results)
# => [<esperanto_analyzer.analyzers.morphological.analyze_result.AnalyzeResult at 0x106888470>, <esperanto_analyzer.analyzers.morphological.analyze_result.AnalyzeResult at 0x106888710>,(...)]

print(first_analyze)
# => <esperanto_analyzer.analyzers.morphological.analyze_result.AnalyzeResult object at 0x106888470>

# Rich and detailed results using `AnalyzeResult`
print(first_analyze.result)
# => <esperanto_analyzer.analyzers.morphological.noun.NounMorphologicalAnalyzer object at 0x106888898>

# Get any information that you might need using the response objects API
print((first_analyze.result.raw_word, first_analyze.result.matches, first_analyze.result.word_class() ))
# => ('Esperanto', <re.Match object; span=(0, 9), match='Esperanto'>, <class 'esperanto_analyzer.speech.noun.Noun'>)

```
---

### Morphological analyze of a single WORD

You can also use the internal analyzers of **words** if you want so, ex:

```py
from esperanto_analyzer.analyzers.morphological import AdjectiveMorphologicalAnalyzer, NumeralMorphologicalAnalyzer

# There's the total of `10` morphological analyzers, such as `VerbMorphologicalAnalyzer`, `NumeralMorphologicalAnalyzer`
analyzer = AdjectiveMorphologicalAnalyzer('belajn')
# If it returns true, that means that the inputed word is a valid adjective. False otherwise
analyzer.analyze() # => returns True/False

print(analyzer.matches)
# => <re.Match object; span=(0, 6), match='belajn'>
print(analyzer.raw_word) # => 'belajn'

# The `word` property is one class object that inherits from the `Word` class.
print(analyzer.word)
# => <esperanto_analyzer.speech.adjective.Adjective at 0x1069079e8>

# Get the base class name for the detected 'Part of Speech' class
print(analyzer.word.__class__.__name__) # => 'Adjective'

numeral_analyzer = NumeralMorphologicalAnalyzer('naŭcent')
numeral_analyzer.analyze() # => True

print(numeral_analyzer.word)
# => <esperanto_analyzer.speech.numeral.Numeral at 0x106964cf8>

print(numeral_analyzer.matches)
# => <re.Match object; span=(0, 7), match='naŭcent'>

```

---

### Parts of Speech:  Word, Article, Adverb, Adjective, Verb...

You can even use the **Parts of Speech**(such as `Article`, `Adverb`, `Pronoun`, `Conjunction`) of the language:

```py
# `esperanto_analyzer.speech` is home for all parts-of-speech classes
from esperanto_analyzer.speech import Article

# Raises an `InvalidArticleError` Exception, since 'lo' is not an Esperanto article
article = Article('lo')

# 'La' is the ONLY valid article in Esperanto
valid_article = Article('la')


# All `esperanto_analyzer.speech` objects inherits from `esperanto_analyzer.speech.word.Word` class
print(valid_article.__class__.__bases__) # => (esperanto_analyzer.speech.word.Word,)

# La is invariable article, it's the same for plural and singular sentences, ex:
# 'La domo' # The house
# 'La domoj' # The houses
print(valid_article.plural) # => False

# You can provide some `context` when creating the `Part of Speech` so it can determine if the word should be in plural or singular, eg:
print(Article('la', 'domoj').plural) # => True


```

---

## Development Setup

Clone this repository:

```bash
$ git clone https://github.com/fidelisrafael/esperanto-analyzer.git
$ cd esperanto-analyzer
```

Make sure you have `python` >= `3.7.0` and  `virtualenv` >= `16.0.0` installed:

```bash
$ python --version
> Python 3.7.0
$ virtualenv --help
> 16.0.0
```

Otherwise, [install it](https://virtualenv.pypa.io/en/stable/installation/).

Then, create one new `virtualenv` and activate it:

```bash
$ virtualenv venv
$ source venv/bin/activate
```

Install the dependencies for development and test enviroments:

```bash
# If you just want to install the needed dependencies for production, just run: `make init`
$ make init_dev
> pip install -r development_requirements.txt
> pip install -r test_requirements.txt
> pip install -r requirements.txt
```

Run the tests:

```bash
$ make test
> pytest tests --cov-config .coveragerc --cov=esperanto_analyzer --cov-report=html
> =============================================================================== test session starts ================================================================================
> platform darwin -- Python 3.7.0, pytest-3.7.4, py-1.6.0, pluggy-0.7.1
> rootdir: /(...)/esperanto_analyzer, inifile:
> plugins: cov-2.5.1
> collected 492 items

> (...)

> ====================================================================== 492 passed, 2 warnings in 2.61 seconds ======================================================================
```

You can follow the code coverage stats opening: `coverage/index.html`

### OBS: This library has **100%** code coverage at the time of this writing!

---

#### Built-in JSON Web API

**_Note: This web API will be published as a separated package in a near future._**

This library cames with a very simple HTTP Server built on top of Flask to provide an WEB API interface for integration with others systems. You can run the HTTP server running the following make task in the root folder of the project:

```bash
$ make web_api # or simply running: python web/runserver.py
> python esperanto_analyzer/web/runserver.py
> * Serving Flask app "esperanto_analyzer.web.api.server" (lazy loading)
> * Environment: production
>   WARNING: Do not use the development server in a production environment.
>   Use a production WSGI server instead.
> * Debug mode: on
> * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Or you can just run it from inside any python project with:

```py
from esperanto_analyzer.web import run_app

run_app(debug=True, port=9090)
# * Serving Flask app "esperanto_analyzer.web.api.server" (lazy loading)
# * Environment: production
#   WARNING: Do not use the development server in a production environment.
#   Use a production WSGI server instead.
# * Debug mode: off
# * Running on http://127.0.0.1:9090/ (Press CTRL+C to quit)

```

This server has auto-reload(or hot-reload) enabled by default, so you don't need to restart the server when you change the source code.

To test it:

```bash
curl http://127.0.0.1:5000/analyze?sentence=Kio%20estas%20Esperanto%3F%20%C4%9Ci%20estas%20lingvo%20tre%20ta%C5%ADga%20por%20internacia%20komunikado.
```


---

## How it works?

This library can be used in a miriad of ways to analyze Esperanto sentences and words, for a complete reference of the API and all the possibilities you should check the 'Full API' section.

[TODO]

---


## :calendar: Roadmap <a name="roadmap"></a>

- :white_medium_small_square: Create syntactical analyzers
- :white_medium_small_square: Update this Roadmap with more plans

---

## :thumbsup: Contributing

Bug reports and pull requests are welcome on GitHub at http://github.com/fidelisrafael/esperanto_analyzer. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](contributor-covenant.org) code of conduct.

---

## :memo: License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
