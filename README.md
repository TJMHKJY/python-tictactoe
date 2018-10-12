# Python TicTacToe

**Installation**  

This project requires Python 3.7.0 which can be downloaded by going here:  
https://www.python.org/downloads/

**Install this project by cloning:**  
```
git clone https://github.com/shibani/python-tictactoe.git
```
___

**To install and run tests**

Install pytest by running 

```
pip install -U pytest
```

cd into root of app directory and run in console.

To run the entire suite:

```
pytest 
```

**To run an individual test file:**
```
pytest tests/ui/test_cli_messages.py -v
```
___ 

**To install run test coverage tools**  

cd into root of app directory and run in console: 

```
pip install pytest-cov  
py.test --cov=python_tictactoe tests/  
```

___ 

**To play game in terminal**

cd into root of app directory and run in console:  

```
python3 -m python_tictactoe
```
___

**Functional Core**

```
python_tictactoe
-- game/  
-- strategy/  
```

**Imperative Shell**
```
python_tictactoe
-- app/  
-- ui/  
``` 
