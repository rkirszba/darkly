# XSS - Stored

## What is it ?

Liste among the OWASP top 10 Web Application Security, Cross Site Scripting (XSS) "occur whenever an application includes untrusted data in a new web page without proper validation or escaping, or updates an existing web page with user-supplied data using a browser API that can create HTML or JavaScript" (OWASP).

There are three main kind of XSS:
	* stored XSS
	* reflected XSS
	* DOM XSS

The stored XSS occurs when the application stores a user input and further reflects it within an HTML output.

## Some use cases

* an attacker leaves a malicious comment (a script) on a trusted website; this script is then reflected on a website page and executed by each visiting user's browser
* stealing of the victim's session ID on the website
* more generally, executing whatever possible script client-side

## Exploit on Darkly

### Context

* there is a `LEAVE A FEEDBACK` part on the website
* the user has to enter his name and his comment that will then be displayed

### Solution

* Name: `a`
* Comment: `<script>alert('xss')</script>`
* this outputs the following flag: `0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E`

## Some ways to avoid it

* never trust the user inputs : validate / filter / sanitize the data sent to the site:
	* generally escape untrusted data depending on the HTML context: use an ""allow list" model, that denies everything that is not specifically allowed" (OWASP)
	* in our example, you could escape every `<` or `>` characters, or remove what stands in between
* encode data on output: for example, in HTML, `<` converts to `&lt;`