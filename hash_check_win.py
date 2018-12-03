#! /usr/bin/env python3.6

import hashlib, sys, os, argparse



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


    # create  a list of arguments passed to the command line
    args = parser.parse_args()

    # store arguments in variables
    inFile = args.file
    alg = args.algorithm + "()"
    key = args.key
    checkSum = ""


    #calculate the checksum
    calcChecksum(inFile, alg)

    # Verify input file if key was given
    verify(checkSum, key)

    # Output results
    results(inFile, alg, key, checkSum )

    print(inFile + '\n' + alg + '\n' + key)

#End main()
    
def calcChecksum(inFile, alg):
    """
    Calculate the checksum of the input file
    """
    # try to open the file, return an error if it fails
    pass

#End calcChecksum()

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
    # If verbosity is specified:

    # No verbosity
    pass

# End results()



if __name__ == '__main__':
    main()

    # def printsumfp(fp, filename, out=sys.stdout):
    # m = md5()
    # try:
    #     while 1:
    #         data = fp.read(bufsize)
    #         if not data:
    #             break
    #         if isinstance(data, str):
    #             data = data.encode(fp.encoding)
    #         m.update(data)
    # except IOError as msg:
    #     sys.stderr.write('%s: I/O error: %s\n' % (filename, msg))
    #     return 1
    # out.write('%s %s\n' % (m.hexdigest(), filename))
    # return 0