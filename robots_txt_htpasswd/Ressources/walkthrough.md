# robots.txt / htpasswd

## What is it ?

* `robots.txt` is a file put at the root of a website in which it is possible to indicate some ressources that are not supposed to be indexed by the search engines.
* `.htpasswd` is a file that contains a list of users, with their (hashed or not) passwords, that are allowed to access a particular page
* this file is generally used in addition to an `.htaccess` file that is stored in the protected directory, and that contains the path to `.htpasswd`


## Exploit on darkly

### Context

* by running `dirsearch` ([github](https://github.com/maurosoria/dirsearch)) on the URL, we find some interesting links:
	* `/admin/`
	* `/robots.txt`

* in `robots.txt`, we find the following links:
	* `/whatever`
	* `/.hidden`

* in `/whatever`, there is file called `htpasswd`

### Resolution

1. `htpasswd` contains: `root:8621ffdbc5698829397d97767ac13db3`
2. Let's decrypt the hexadecimal part on [dcode](https://www.dcode.fr/fonction-hash#f0): we get `dragon`
3. Let's try to connect as `root` with password `dragon`: it works and we get the flag `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

## Some ways to avoid it

* by using tools like `dirsearch` a user can find some paths that are not directly referenced while navigating "normally" in the website / by the search engines
* better configure the `.htaccess` / `.htpasswd` part
* use better hash for anything involving a password
* for such a sensitive part as the `admin` one, use a much stronger password than `dragon`

