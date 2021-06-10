# Cookie privilege escalation

## What is it ?

Cookies can be used to define roles, or access rights.
As a user, it is possible to modify the value of a cookie field in order to escalate privilege.

## Exploit on Darkly

### Context

* the cookie name is `I_am_admin` and its value is `68934a3e9455fa72420237eb05902327`
* we will try to figure out what `68934a3e9455fa72420237eb05902327` means and then change the value

### Solution

1. on [dcode](https://www.dcode.fr/fonction-hash#f0), we decrypt `68934a3e9455fa72420237eb05902327`, what gives `false` (it was `MD5` hashed)
2. we suppose that we have to set the value as an `md5` hash of `true`, that is to say `b326b5062b2f0e69046810717534cb09`
3. Changing the cookie value and reloading the page, we get a flag: `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

## Some ways to avoid it

* do not refer to the privileges of the user in the cookie
* do not make possible to identify oneself as someone else by changing the value of a cookie attribute