# Recover password flaw

## Exploit on Darkly

### Context

* on the `I forgot my password` page, there is only a `SUBMIT` button.
* when clicking on it, it outputs a `Sorry Wrong Answer` image
* when inspecting the page, we can see that `SUBMIT` is part of a form, submitted with a `POST` request
* another input, of `hidden` type refers to an email address

### Solution

1. The mail address is sent in the body of the `POST` request
2. Let's change the mail address (for example directly in the `Elements` part of `inspect`) and `SUBMIT` it
3. We get the flag: `1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0`

## Some ways to avoid it

* don't think that a user won't see an element in a form only because it is of `hidden` type, as he can see it by reading the HTML code
* don't trust any element of a request as the user can modify them
* in this particular case, e-mail address should for instance have been hardcoded directly in the backend part of the website