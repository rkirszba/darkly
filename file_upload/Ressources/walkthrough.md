# File Upload attack

## Some use cases

The file upload can cause several problems:
	* erase a sensitive file
	* occupy too much space on the server
	* execute malicious code...

## Exploit on Darkly

### Context

* on the `ADD IMAGE` page, we can upload a file.
* as far as we could test, only .jpeg and .png can be uploaded
* our goal will be to upload a php file, for example

### Solution

1. Looking at the `network` part of `inspect`, we can see that the file is sent as part of a `multipart/form-data` (see request headers). For more details we can see the body of the request:
```
Content-Disposition: form-data; name="uploaded"; filename="test.jpg"
Content-Type: image/jpeg
```
2. In [form.py](./form.py), we make a request that will send a php file while pretenting sending a jpeg one:

3. We get the flag: `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`

## Some ways to avoid it

* do not trust the request body as it can be modified by the attacker
* list allowed extensions (and be careful with all the techniques intented at bypassing it)
* validate the file type

