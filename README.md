# Hash in Batch
Script to generate hashes in batch from a plain text file. Useful for brute force cracking.
Output directed to stdout for easier commandline integration.


##### USAGE:
> python hash.py "file-name" "hash-type"


##### SUPPORTED HASHES:
> md5, md4, ntlm
> 
> sha1, sha224, sha256, sha384, sha512
> 
> blake2b, blake2s


##### EXAMPLE:
`python hash.py hashme.txt md5 > hashes.txt`
> 
> hashme.txt:
```
password123
jeremyberemy
iloveyou
````
> 
> hashes.txt
```
482c811da5d5b4bc6d497ffa98491e38 --> password123
5472776b0d5911c9a918eb4ea82e324d --> jeremyberemy
f25a2fc72690b780b2a14e140ef6a9e0 --> iloveyou
```

