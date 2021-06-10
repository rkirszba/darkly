# Unvalidated redirects

## What is it ?

Previously listed among top 10 Web Application Security Risks, unvalidated redirects occur when "when a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input." (OWASP) 

## Use cases

1. an attacker sends a link towards a trusted website to its victim
2. there is a malicious site in the redirect parameter of the url
3. the trusted website redirects towards the malicious website
4. for example, the malicious website has exactly the same UI as the trusted one and asks for credentials (phishing)

## Exploit on Darkly

### Context

* on the footer of each page of the site, we can see icons of Facebook, Twitter and Instagram

* inspecting the HTML code allows to see that that those icons point to `index.php?page=redirect&site=facebook` (or `twitter` or `instagram`)

### Solution

* in `inspect`, let's try to change `site=facebook` to `site=www.lequipe.fr`: we get the following flag: `B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3`

* we can imagine that there is a special handling for the above sites, otherwise the website redirects to the url provided in parameter

## Some ways to avoid it

* if possible, do not use redirects
* set up a whitelist of sites you can redirect to
* use a hash for redirect addresses
