## Survey hijacking

## Exploit on Darkly

### Context

* on the `SURVEY` part of the site, it is possible to rate 6 different people from 1 to 10.
* the average grade of the first user is much higher than 10. Is it possible to give someone an higher grade than 10 ?

### Solution

* we can `inspect` this survey and change the value of a grade to, for example `100000`.
* when clicking on this grade, we get the flag: `03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA`

## Some ways to avoid it

* never trust the data sent by a user request
* check that the sent grade stands between 1 and 10