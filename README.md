# flask-api-boilerplate
A Flask api template

### Summary
1. This is an api project template based on flask [method views](https://flask.palletsprojects.com/en/2.0.x/views/).
2. Code is tested on >=python3.9 and MacOS environment. Windows environments or lower python versions will need some tweaking.

### Configuration
- Add your app configuration to the root of the project as a `.env` file. If using a different env file name, update server.py.
- Update `app.utilities.AppConfig` class with any extra keys added to env file.

### Running the app
Install dependencies. This will also create a virtualenvironment if none exists.  
```
make install-deps
```  

Run with make.
```
make run-dev
```  


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