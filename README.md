# Flask API Boilerplate
A Flask api template

### Summary
1. This is an api project template based on flask [method views](https://flask.palletsprojects.com/en/2.0.x/views/).
2. Code is tested on >=python3.9 and MacOS environment. Windows environments or lower python versions will need some tweaking.

### Configuration
- Add your app configuration to the root of the project as a `.env` file. If using a different env file name, update server.py. You MUST provide `SQLALCHEMY_DATABASE_URI` string in the `.env` file. A convenient service I use for test postgresql databases is [ElephantSQL](https://www.elephantsql.com/). On creating a free db instance you will get a database uri that you can copy into your env file.
- Update `app.utilities.AppConfig` class with any extra keys added to env file.

### Running migrations
[Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) is used to manage database migrations.

Start by installing dependencies with `make install-deps`.

Initialize migrations. This will create a `./migrations/` folder.
```
make init-migrations
```
After making changes to `models.py`, track those changes with:
```
make migrate
```
Finally apply migrations to database with:
```
make upgrade
```
The commands above are just a thin wrapper around flask migrate cli commands.


### Running the app
Install dependencies. This will also create a virtualenvironment if none exists.  
```
make install-deps
```  

Run with make.
```
make run-dev
```

Alternatively, you can run  the app with docker. This command will invoke docker-compose.
```
make run
```

Stop the containers running in the background with:
```
make stop
```

On start, one test endpoint will be available.
```
curl --location --request POST 'http://127.0.0.1:8000/hello' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Habari",
    "language: "Swahili"
}'
```
Response:
```
{
    "greeting": {
        "id": 1,
        "language": "Swahili",
        "name": "Habari"
    },
    "message": "Successfully added new greeting"
}
```

```
curl --location --request GET 'http://127.0.0.1:8000/hello'
```
Response:
```
{
    "data": [
        {
            "id": 1,
            "language": "Swahili",
            "name": "Habari"
        }
    ],
    "message": "Success"
}
```

### Running Tests
Run unit and integration tests with:
```
make run-tests
```

Alternatively, you can run each separately with `make unit-test` and `make int-test`.

### Code Formatting
This project uses the [black](https://black.readthedocs.io/en/stable/) code formatter with the default configuration.
To check which files would be reformatted:  

```
make format-check
```  

To format:
```
make format
```  


**Naming is hard, consider renaming things as you see fit.**