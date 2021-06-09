# Broken Authentication

## Definition

Listed among the OWASP top 10 Web Application Security Risks, Broken Authentication allows "attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users’ identities temporarily or permanently" (OWASP)

## Some use cases

* act as the admin of the website
* on a e-commerce website, buy stuff with another users's account

## Exploit on Darkly

### Context

* While practicing SQL injections, we found a table schema called `Member_Brute_Force` with a unique table `db_default`.
* On the `MEMBERS` page, inputing `1 AND 1=2 UNION SELECT username, password FROM Member_Brute_Force.db_default` gives two results:
	* root and `3bf1114a986ba87ed28fc1b5884fc2f8`
	* admin and `3bf1114a986ba87ed28fc1b5884fc2f8`

### Solution

* First Solution: trying to reverse the hash
	1. on [dcode](https://www.dcode.fr/fonction-hash#f0), we decrypt `3bf1114a986ba87ed28fc1b5884fc2f8`, what outputs `shadow`
	2. We try this password with `root` and `admin` and it works in both case

* Second Solution: bruteforce
	1. We download a list of [common passwords](https://github.com/DavidWittman/wpxmlrpcbrute/blob/master/wordlists/1000-most-common-passwords.txt#L14)
	2. As the name of the table schema invites us, we bruteforce `root` or `admin` with the [bruteforce.py](./bruteforce.py) script, that tries asynchronously each passwords on the `SIGN IN` part of the site
	3. We try this password with `root` and `admin` and it works in both case

* The flag is `B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2`

## Some ways to avoid it

* use multi-factor authentication
* implement weak-password checks
* do not expose sensitive data such as list of users and (even hashed passwords)
* use strong password hashes (in our case, the password was `MD5` hashed, what is no longer considered cryptographically secure)