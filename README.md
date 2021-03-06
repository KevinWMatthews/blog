# Kevin's Blog

Platform for my projects.

## Getting Started

Basic instructions for development.

### Requirements

* Python
* virtualenv

### Setup

Create and activate a virtual environment
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Install requirements
```
$ pip install -r requirements.txt
```

### Configuration

Using `python-dotenv` package.
Configuration is done in `.flaskenv` and `.env`.
```
FLASK_ENV=development           # Enable debug mode using Werkzeug
# or
FLASK_ENV=production            # Run with production servers
```


### Run

Run flask development server:
```
$ flask run
```

Generate static content for deployment to Netlify:
```
$ python blog.py --deploy
```

Frozen-Flask puts files in `app/build` by default.
