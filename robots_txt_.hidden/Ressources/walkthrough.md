# robots.txt / .hidden

## What is it ?

* `robots.txt` is a file put at the root of a website in which it is possible to indicate some ressources that are not supposed to be indexed by the search engines.

# Exploit on darkly

### Context

* by running `dirsearch` ([github](https://github.com/maurosoria/dirsearch)) on the URL, we find some interesting links:
	* `/admin/`
	* `/robots.txt`

* in `robots.txt`, we find the following links:
	* `/whatever`
	* `/.hidden`

* in `.hidden`, there are a lot of links pointing to another page with a lot of links, etc. In each page, there is also a `README`, that contains trolling sentences. Exploring manually all the links would take a very long time

### Solution

1. Set up a [crawler script](./crawler.py) that browses all the links and outputs the content of `README` if it is not one the known trolling sentences
2. We get a flag: `99dde1d35d1fdd283924d84e6d9f1d820`

## Some ways to avoid it

* don't leave sensitive data on the website even if it is a needle in a haystack