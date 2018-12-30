import hashlib
 

def getAlg(choice):
    """
    Set the correct hash algorithm based on user input
    """
    if choice == 'md5':
        return hashlib.md5()
    elif choice == 'sha1':
        return hashlib.sha1()
    elif choice == 'sha224':
        return hashlib.sha224()
    elif choice == 'sha256':
        return hashlib.sha256()
    elif choice == 'sha384':
        return hashlib.sha384()
    elif choice == 'sha512':
        return hashlib.sha512()
    elif choice == 'blake2b':
        return hashlib.blake2b()
    elif choice == 'blake2s':
        return hashlib.blake2s()

def calcChecksum(inFi, hashAlg, bufsiz):
    """
    Calculate the checksum of the input file
    """
    try:
        with open(inFi, 'rb') as f:
            # Read each byte of the file using the specified buffer size
            while True:
                data = f.read(bufsiz)
                if not data:
                    break
                # add each section of bytes to the hash algorithm
                hashAlg.update(data)
            # Generate the checksum for the input file
            cksum = hashAlg.hexdigest()
        return cksum
    # print any errors that occur
    except IOError as msg:
       print('\nI/O error: %s\n' % (msg))