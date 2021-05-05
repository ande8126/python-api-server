# Exploring Python

## Setup 

MacOS already has a version of python installed. However it is likely a version of python 2 and the students will want to be working with python 3. 

### Homebrew Python Install 

Install python version 3:

```
brew install python
```

> If you get the following `Error: Permission denied @ dir_s_mkdir - /usr/local/Frameworks`, it can be fixed by doing the following:
>
>
>- `sudo mkdir /usr/local/Frameworks`
>- `sudo chown $USER /usr/local/Frameworks`


If `sudo` isn't allowed, you can also try:

>install -d -o $(whoami) -g admin /usr/local/Frameworks

Then,

>brew reinstall python

---

## Running

Homebrew sets up python 3 as a separate executable, which keeps it from conflicting with the MacOS version. That's awesome, but means instead of using `python` and `pip` you need to run `python3` and `pip3`.

`Pip` is the package manager for Phython, like `npm` for Node.

Check that they both work:

```
python3 --version
pip3 --version
```


## Basic Hello World

Create a new file called `hello_world.py`:

``` Python
print("Hello, World! Woot!")
```

Then we can run it:
```
python3 hello_world.py 
```


Making it a function:

``` Python
def hello():
  print("Hello, World! Woot!")

hello()
```


## Web Hello World

For a web Hello World, we'll use [Flask](http://flask.pocoo.org/). 

Create a new file `hello_web.py`:

``` Python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Woot!"
```

We need to install flask:

```
pip3 install Flask
```

Run the app:

```
FLASK_APP=hello_web.py flask run
```

Check it out at: http://localhost:5000/


## API Example

Run the `api-example.py` file: `$ python3 api-example.py`

See the app at:

> http://localhost:5000/

### Routes

- `GET /` : returns an HTML message
- `GET /api/books/all` : returns all books in the array (as JSON)

### Resources

Based on this more robust tutorial which includes DB integration: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#setting-up

## API with Database

Run the `api-with-db.py` file: `$ python3 api-with-db.py`

### Routes

- `GET /` : returns an HTML message
- `GET /api/books/all` : returns all books in the DB (as JSON)
- `POST /api/books/add` : inserts a book to the DB


### PostGRES/psychopg2
- https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/

### Flask
- http://flask.pocoo.org/docs/1.0/quickstart/

## Known pitfalls/troubleshooting
Odd compile error when running `pip3 install psycopg2`
https://github.com/psycopg/psycopg2/issues/492
Probably a caching issue. Running `pip3 install -i https://testpypi.python.org/pypi psycopg2==2.7.7` worked
