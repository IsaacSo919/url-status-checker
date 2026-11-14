The tool is designed for IT support staff to help investigate basics website connectivity  problems.
The input is a URL
The output is the  HTTP status code or a connection error message.

Installation:
Run the follow command in cmd:
    py -m venv .venv
    .venv\Scripts\activate.bat
    python -m pip install -r requirements.txt

Usage：
    python checker.py
    then input a full URL with https:// or http://

## Tests

Run the unit tests from the project directory:

```bat
python -m unittest -v
```

These tests check the descriptions for status codes 404 and 418.

## Limitations

The tool checks HTTP responses, but it does not test website
features such as login or checkout.

A timeout does not tell us the exact cause of the problem.

The current unit tests only check the descriptions for status
codes 404 and 418.
## Future improvements

I would add automated tests for request handling, including
timeouts and connection errors. These tests would use simulated
responses and exceptions so they do not depend on live websites.