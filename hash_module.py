import hashlib
 

def calcChecksum(inFi, alg, bufsiz):
    """
    Calculate the checksum of the input file
    """
    hashAlgs = {
    'md5': hashlib.md5(),
    'sha1': hashlib.sha1(),
    'sha224': hashlib.sha224(),
    'sha256': hashlib.sha256(),
    'sha384': hashlib.sha384(),
    'sha512': hashlib.sha512(),
    'blake2b': hashlib.blake2b(),
    'blake2s': hashlib.blake2s(),
                } # end hashAlgs

    # Select the hash algorithm to use
    hashAlg = hashAlgs[alg]

    try:
        with open(inFi, 'rb') as f:
            # Read sections of the file using the specified buffer size
            while True:
                data = f.read(bufsiz)
                if not data:
                    break  # end the loop when the file has been completely read
                # add each section of bytes to the hash algorithm
                hashAlg.update(data)
            # Generate the checksum for the input file
            cksum = hashAlg.hexdigest()
        return cksum
    # print any errors that occur while opening or processing the file
    except IOError as msg:
       print('\nI/O error: %s\n' % (msg))
    # end calcChecksum