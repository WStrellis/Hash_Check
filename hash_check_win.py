#! /usr/bin/env python3.7

import argparse

# get the default buffer size of the system
from io import DEFAULT_BUFFER_SIZE as getSysBuffSize

# Used to seperate file name from the rest of the path
from os.path import split as pathSplit

from hash_module import calcChecksum
from verify_module import verify
from results_module import results


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
                        help="The algorithm used to generate a checksum. Lowercase characters only. If unspecified, the default algorithm is sha256",)

    # Verification key
    parser.add_argument("-k", "--key",
                         default='',
                         type=str,
                         help="A key used to verify the integrity of the input file")

    # Buffer size 
    parser.add_argument("-b", "--buffer",
                         default= getSysBuffSize,
                         type=int,
                         help="The buffer size used to read the input file. If unspecified, the system's default buffer size will be used.")

    # Verbosity
    parser.add_argument("-v", "--verbose",
                         help="Enable more detailed output messages.",
                         action="store_true")

    # create  a list of arguments passed to the command line
    args = parser.parse_args()

    #calculate the checksum
    checkSum = calcChecksum(args.file, args.algorithm, args.buffer)

    if checkSum:

        # Validate input file. Will set 'valid' to 'False' if no verification key is entered.
        valid = verify(checkSum, args.key)

        # seperate the file name from the rest of the path
        fileName = pathSplit(args.file)[1]
        results(fileName, args.algorithm,  checkSum.upper(),args.key.upper(), valid, args.verbose )

#End main()
    

if __name__ == '__main__':
    main()
