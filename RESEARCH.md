Task 1
## Handling HTTP timeouts



\### What I needed to learn



How to set a timeout and handle a request that takes too long.



\### Sources I read

\- ChatGPT explanations and examples.

\- Requests Quickstart: https://requests.readthedocs.io/en/latest/user/quickstart/

&#x20; Sections read: Make a Request and Response Status Codes.



\### What I tested

I requested https://httpbin.org/delay/10 with timeout=5.



\### Actual result

The program printed:

"Request timed out. The cause is not yet known."



\### What I learned and limitations

The Timeout exception handler displayed my message.

A timeout alone does not tell me the cause of the problem.

This was one manual test using a public service.

Task 2
Question: example.com  MissingSchema

Decision: Just remind user  to add "https://"

Verifiy: Succssful


