import hashlib
import sys

file_name = str(sys.argv[1])  #file-name

hash_type = str(sys.argv[2]).lower()  #hash-type


with open(sys.argv[1], "r") as f:
    
    
    #md5
    if hash_type == 'md5':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.md5(line.encode()).hexdigest()} --> {line}')
            
    #md4
    elif hash_type == 'md4':
        
        for line in f:
            
            line = line.strip()
            hashyboy = hashlib.new('md4', line.encode())
            hash = hashyboy.hexdigest()
            print(hash + ' --> ' + line)
            
    #sha1
    elif hash_type == 'sha1':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.sha1(line.encode()).hexdigest()} --> {line}')
               
    #sha224
    elif hash_type == 'sha224':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.sha224(line.encode()).hexdigest()} --> {line}')
            
    #sha256
    elif hash_type == 'sha256':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.sha256(line.encode()).hexdigest()} --> {line}')
            
    #sha384
    elif hash_type == 'sha384':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.sha384(line.encode()).hexdigest()} --> {line}')
            
    #sha512
    elif hash_type == 'sha512':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.sha512(line.encode()).hexdigest()} --> {line}')
            
    #blake2b
    elif hash_type == 'blake2b':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.blake2b(line.encode()).hexdigest()} --> {line}')
            
    #blake2s
    elif hash_type == 'blake2s':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.blake2s(line.encode()).hexdigest()} --> {line}')
            
    #sha1
    elif hash_type == 'sha1':
        
        for line in f:
            
            line = line.strip()
            print(f'{hashlib.sha1(line.encode()).hexdigest()} --> {line}')
    #ntlm
    elif hash_type == 'ntlm':
        
        for line in f:
            
            line = line.strip()
            hashyboy = hashlib.new('md4', line.encode('utf-16le'))
            hash = hashyboy.hexdigest()
            print(hash + ' --> ' + line)
            
            
    #uupsy wuupsy
    else:
        
        print('\nUsage: python hash.py "file-name" "hash-type"')
        print('\nSUPPORTED METHODS:\n')
        print('md5, md4, ntlm')
        print('sha1, sha224, sha256, sha384, sha512')
        print('blake2b, blake2s')
