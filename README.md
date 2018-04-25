# Similar Japanese words sorted by frequency (API)

When you specify a search word and make a request to this API, it will respond with synonym word names and  frequencies with reference to the DB in advance.

(DB: for example, analyzing word frequencies by decomposition Part-of-speech from item descriptions of a certain company)

## Getting Started

1. [Download the Database of similar words dictionary (sqlite)](http://compling.hss.ntu.edu.sg/wnja/index.ja.html)

1. Store the downloaded wnjpn.db file under ./db/

1. Create a csv file that extracts the word names and frequencies from a specific person or site whose trends you want to analyze.

1. Rename the created csv file into all.csv, and store it under ./csv/word_ranking/

### Prerequisites

* Environment Requirements: python 3.6.2

* [Front-End](https://github.com/atsushieee/similar-word-front)

### Installing

``` bash
# install dependencies
pip install -r requirements.txt
```

## Running the tests

``` bash
# serve with hot reload at localhost:5000
python app.py
```

## Deployment

The following files are required for deployment to Heroku

* runtime.txt - Description of python's executive environment

* uwsgi.ini - Init file for running Flask application on heroku

* Procfile - Run application via uWSGI

## Authors

* **Atsushi Tabata**  [Private URL](https://ippoippo.info)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
