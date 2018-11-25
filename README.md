# Personal website

This will be my website.

## Getting Started

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

Generate static content and server:
```
$ python blog.py --test
```

Generate static content only:
```
$ python blog.py --build
```

Frozen-Flask puts files in `app/build` by default.



## Links

  * [Adobe Color](https://color.adobe.com/create/color-wheel/)
  * Javascript Visualizations using [PTS](https://ptsjs.org/)
