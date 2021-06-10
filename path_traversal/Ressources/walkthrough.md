# Path Traversal

## What is it ?

"A path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder." (OWASP)

## Some use cases

* access sensitive data anywhere on the web application server

## Exploit on Darkly

### Context

* each page in the site tree structure is accessed by using a `page` parameter in the url

* when a random value is set for this parameter, an alert `WTF ?` pops up

### Solution

1. We first try `page=/etc/passwd`: it does not work
2. We then try `page=../../etc/passwd`: the alert is not the same as usual
3. We use [page.py](./page.py) script to bruteforce the parameter by adding at each try `../` before `etc/passwd`. The working path is `page=../../../../../../../etc/passwd`
4. We try it directly on the website and we get the following flag: `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

## Some ways to avoid it

* never trust the user input: sanitize it before using it:
	* blacklisting characters like `../` could be not enough as it is possible to bypass it
	* make sure user can not provide the complete path
* ensure to give appropriate rights to the user running the web application
