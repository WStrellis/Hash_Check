#!/usr/bin/python3

# A program for storing passwords

import sys 
import hashlib
algorithms = ['sha1','sha224','sha256','sha384','sha512', 
		      'blake2b','blake2s','md5']

alg = sys.argv[1]
thing = sys.argv[2]
good = sys.argv[3]

def getHash(alg,thing):
	"""Calculates the hash value of "thing" using "alg". """
	h = hashlib.new(alg)
	h.update(thing)
	return h.hexdigest()

def checkHash(alg,thing,good):
	""" Peforms the hash check"""
	if getHash(alg,thing) == good:
		print("Postitive Match")
	else:
		print("Error! {} sum of {} does not match {}".format(alg,thing,good))

if len(sys.argv) < 4 or sys.argv[1] not in algorithms:
	print('Usage: hash_check.py [algorithm] [file to hash] [correct hash]\n\
    \rUse [algorithm] to create a hash for [file to hash]. Compare the result\
 to [correct hash].\n \
	 \rSupported algorithm arguments:\n\r%s' %(' '.join(algorithms)))

# print(hashlib.md5(b"hello").hexdigest())
 
checkHash(alg,thing,good)