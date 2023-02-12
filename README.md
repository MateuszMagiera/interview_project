## Requirements 
All the necessary requirements, are inside the requirements.txt file. \
To install the necessary requirements, run :
``` 
pip install -r requirements.txt

```

## Run single test
In order to run a specific test, run 
```
pytest -v tests/test_name.py
```

## Run collection of tests
In order to run a collection of tests, run
```
pytest -v tests/
```

## Run test in a different browser
In the current stage there is only a possibility to run the tests in two different browsers, the Google Chrome is \
set up as the default browser. In order to run the test (or the collection of tests) in the Firefox browser, run
```
pytest -v tests/test_name.py --browser_name=firefox
```
## Run the test and generate the report
In order to run the test, or the collection of tests, and generate a report run:
```
pytest -v tests/ --html=./Reports/report.html

```