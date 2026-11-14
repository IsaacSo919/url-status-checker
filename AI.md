# AI Usage

## Tool used

ChatGPT

## How I used AI

AI helps me like wikipedia, explaining important concepts.

## Incorrect or unhelpful suggestions

ChatGPT suggested creating a fresh virtual environment while my
existing environment was active. The command failed with
"Unable to create process". The next installation command then
failed because the new environment had not been created.

I deactivated the existing environment and explicitly selected
Python 3.14 to create the new environment successfully.
The exact cause of the original failure was not confirmed.

I learned to check that each command succeeds before continuing
with commands that depend on it.

## How I verified suggestions
I just worked that out and test it.

### Manual checks

I have checked successful response, missing scheme, invalid URL,
connection failure, timeout and redirect.

### Unit tests

tested status418 and status 404

### Installation check

I created a fresh virtual environment named .venv-check using
Python 3.14. I installed the dependencies from requirements.txt
and ran checker.py using that environment's Python.

I checked https://example.com and confirmed that the program
displayed an HTTP response.

## My understanding and responsibility

I used AI explanations and code examples while building the tool.
I reviewed and adapted the suggestions, ran the program, and
checked its behaviour with manual checks and unit tests.

I learned to distinguish HTTP status codes from connection
exceptions. I also learned that a timeout does not identify the
root cause, and that the final status code may follow redirects.

I am still developing my understanding of HTTP and automated
testing. Further improvements could include handling more
request errors and adding tests for the request-handling logic.