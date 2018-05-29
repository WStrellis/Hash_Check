#!/usr/bin/python3

# A program for storing passwords

import sys 
import hashlib
import io  # Used to determine buffer size of system

algorithms = ['sha1','sha224','sha256','sha384','sha512', 
		      'blake2b','blake2s','md5']


alg = sys.argv[1]
fileX = sys.argv[2]
good = sys.argv[3]

def getHash(alg,fileX):
	"""Calculates the hash value of "fileX" using "alg". """
	h = hashlib.new(alg)
	try:
		with open(fileX,'rb',buffering=io.DEFAULT_BUFFER_SIZE) as fx:
			h.update(fx)
		return h.hexdigest()
	except FileNotFoundError:
		return "!"

def checkHash(alg,fileX,good):
	""" Peforms the hash check"""
	if getHash(alg,fileX) == good:
		print("Postitive Match")
	elif getHash(alg,fileX) == "!" : 
		print("File Not Found")
	else:
		print("Error! {} sum of {} does not match {}".format(alg,fileX,good))

if len(sys.argv) < 4 or sys.argv[1] not in algorithms:
	print('Usage: hash_check.py [algorithm] [file to hash] [correct hash]\n\
    \rUse [algorithm] to create a hash for [file to hash]. Compare the result\
 to [correct hash].\n \
	 \rSupported algorithm arguments:\n\r%s' %(' '.join(algorithms)))

checkHash(alg,fileX,good)