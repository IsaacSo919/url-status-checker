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


Task 3

\## Invalid URLs



\- Input tested: https://

\- Original result: InvalidURL — No host supplied.

\- Change: Added an InvalidURL exception handler.

\- Retest result: The program displayed a helpful message without a traceback.



\## Redirects



\- http://example.com returned 200 with 0 redirects.

\- https://httpbin.org/redirect/1 returned 200 with 1 redirect.

\- The final URL was https://httpbin.org/get.

\- I learned that a changed URL alone does not prove a redirect.

&#x20; response.history records the redirect responses.

