#! /usr/bin/env python3.7

import hashlib, sys, os, argparse, io
from hash_module import calcChecksum, getAlg


def main():


    # *********************** Evaluate User Input *************
    parser = argparse.ArgumentParser(description="A program used to calculate checksum values for a file. It may also be used\
    to verify the integrity of a file")

    # The file that will be checked
    parser.add_argument("file", help="The path to the file which needs verification") 

    # The algorithm to use for generating a checksum
    parser.add_argument("-a", "--algorithm",
                        choices=["sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "md5"],
                        default="sha256",
                        help="The algorithm used to generate a checksum. Lowercase characters only.",)

    # Verification key
    parser.add_argument("-k", "--key",
                         type=str,
                         default= "",
                         help="A key used to verify the integrity of the input file")

    # Buffer size 
    parser.add_argument("-b", "--buffer",
                         default= io.DEFAULT_BUFFER_SIZE,
                         type=int,
                         help="The buffer size used to read the input file")


    # create  a list of arguments passed to the command line
    args = parser.parse_args()

    # store arguments in variables
    inFile = args.file
    alg = args.algorithm
    key = args.key
    bSize = args.buffer

    # Set the correct hashing algorithm
    hashSelection = getAlg(alg)

    #calculate the checksum
    checkSum = calcChecksum(inFile, hashSelection, bSize)

    # Verify input file if key was given
    verify(checkSum, key)

    # Output results
    if checkSum:
        results(inFile, alg, key, checkSum )

    # print(inFile + '\n' + alg + '\n' + key)

#End main()
    

def verify(checkSum, key):
    """
    Compare the calculated checksum to the verification key
    """
    pass

# End verify()

def results(inFile, alg, key, checkSum ):
    """
    Display the results of the program
    """
    print(checkSum)
    # If verbosity is specified:

    # No verbosity
    # print("\n{!s1} checksum : {!s2}".format( inFile, checkSum))

# End results()



if __name__ == '__main__':
    main()
