#! python

# A program for storing passwords

import sys 
import hashlib
algorithms = ['sha1()','sha224()','sha256()','sha384()','sha512()', \
		      'blake2b()','blake2s()','md5()']
if len(sys.argv) < 4 or sys.argv[1] not in algorithms:
	print('Usage: hash_check.py [algorithm] [file to hash] [correct hash]\n\
    \rUse [algorithm] to create a hash for [file to hash]. Compare the result\
 to [correct hash].\n \
	 \rSupported algorithm arguments:\n\
	 \r%s' %(' '.join(algorithms)))
	# print(algorithms,end=None)
	

	# sys.exit()

print(hashlib.md5(b"hello").hexdigest())