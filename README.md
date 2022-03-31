# muchhash
Script to generate hashes in batch from a plain text file. Useful for brute force cracking.


#####USAGE:
> python hash.py "file-name" "hash-type"


#####SUPPORTED HASHES:
> md5
> 
> NTLM (md4, utf-16le encoding)
> 
> other stuff ill get to later


#####EXAMPLE:
> python hash.py hashme.txt md5

hashme.txt:
```
password123
jeremyberemy
iloveyou
````

stdout:
