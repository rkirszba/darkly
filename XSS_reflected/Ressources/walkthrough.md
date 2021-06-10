# XSS - Reflected

## What is it ?

Liste among the OWASP top 10 Web Application Security Risks, Cross Site Scripting (XSS) "occur whenever an application includes untrusted data in a new web page without proper validation or escaping, or updates an existing web page with user-supplied data using a browser API that can create HTML or JavaScript" (OWASP).

There are three main kind of XSS:
	* stored XSS
	* reflected XSS
	* DOM XSS

The reflected XSS occurs when the application includes (reflects) some of the user input in its HTML output.

## Some use cases

* an attacker can send to his victim a malicious link towards a website the victim trusts; "malicious" means, for example, adding some script in a parameter of the URL that will be then reflected by the application and executed client-side
* stealing of the victim's session ID on the website
* more generally, executing whatever possible script client-side

## Exploit on Darkly

### Context

* One of the pictures on the main page is clickable
* the URL looks like this : `http://[IP]/?page=media&src=nsa`
* when we change the `src` parameter value to another one, it gets reflected in the HTML code. For example, if we do `http://[IP]/?page=media&src=hey`, some part of the HTML code is `<object data="hey">`
* The `object` tag is used to embed objects like audio, video, pdf, etc. in an HTML document ; the `data` attribute is generally used to store a URL. Could we put a script ?

### Solution

We try several to reflect several elements, most of them inspired by [hacktricks](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting)

1. Use of `javascript:` protocol: `http://[IP]/?page=media&src=javascript:alert('xss')`: this does not work as the `javascript` part is not reflected by the application

2. Use of HTML text: `http://[IP]/?page=media&src=data:text/html,<script>alert('xss')</script>`: this works (an `XSS` alert pops up) but for whatever reason we don't get the flag

3. Obfuscation of the script: `http://[IP]/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgneHNzJyk8L3NjcmlwdD4=` where `PHNjcmlwdD5hbGVydCgneHNzJyk8L3NjcmlwdD4=` is the base64 encoding of `<script>alert('xss')</script>`. It works and we get the flag: `928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D`

## Some ways to avoid it

* never trust the user inputs : validate / filter / sanitize the data sent to the site:
	* generally escape untrusted data depending on the HTML context: use an ""allow list" model, that denies everything that is not specifically allowed" (OWASP)
	* in our example check if a protocole like `data` or `javascript` is used
* encode data on output: for example, in HTML, `<` converts to `&lt;`