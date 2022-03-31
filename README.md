# muchhash
Script to generate hashes in batch from a plain text file. Useful for brute force cracking.


##### USAGE:
> python hash.py "file-name" "hash-type"


##### SUPPORTED HASHES:
> md5
> 
> NTLM (md4, utf-16le encoding)
> 
> other stuff ill get to later


##### EXAMPLE:
> python hash.py hashme.txt md5

hashme.txt:
```
password123
jeremyberemy
iloveyou
````

stdout:
482c811da5d5b4bc6d497ffa98491e38 --> password123
5472776b0d5911c9a918eb4ea82e324d --> jeremyberemy
f25a2fc72690b780b2a14e140ef6a9e0 --> iloveyou
