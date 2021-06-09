# User-agent / Referer spoofing

## What is it ?

In a header request, it is possible to indicate:
* a `User-agent`: the web-browser that is used
* a `Referer`: identifies where the request originated from. It could be used by websites for:
	* analyzing purpose
	* serving different content depending on the referer information

## Use cases

* modifying the expected behaviour of the website
* enhance the probability to succeed in Cross-Site Request Forgery attack

## Exploit on darkly

### Content

* on the page pointed by the footer `© BornToSec`, `inspect` allows us to see a long comment
* Two elements in this comment are relevant:
	* `You must cumming from : "https://www.nsa.gov"`
	* `Let's use this browser : "ft_bornToSec"`

### Solution

1. In header modifier, let's set up the `User-agent` field as `ft_bornToSec` and the `Referer` one as `https://www.nsa.gov`
2. By refreshing the page, we get the flag: `F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188`

### Some ways to avoid

* don't rely on either `User-agent` or `Referer` for sensitive tasks

