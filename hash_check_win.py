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

    # Buffer size 
    parser.add_argument("-b", "--buffer",
                         default=8096,
                         type=int,
                         help="The buffer size used to read the input file")


    # create  a list of arguments passed to the command line
    args = parser.parse_args()

    # store arguments in variables
    inFile = args.file
    alg = args.algorithm + "()"
    key = args.key
    bSize = args.buffer


    #calculate the checksum
    checkSum = calcChecksum(inFile, alg, bSize)

    # Verify input file if key was given
    verify(checkSum, key)

    # Output results
    results(inFile, alg, key, checkSum )

    print(inFile + '\n' + alg + '\n' + key)

#End main()
    
def calcChecksum(inFi, a, bfs):
# def calcChecksum():
    """
    Calculate the checksum of the input file
    """
    try:
        with open(inFi, 'rb') as f:
            data = f.read(bfs)
            a.update(data)
    #  Return an error if the file cannot be opened
    except IOError as msg:
        print('%s: I/O error: %s\n' % (inFi, msg))
    cs = a.hexdigest()
    return cs

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
    print("""
    \n{!s1} checksum : {!s2}
    """).format( inFile, checkSum)
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

    # with open("D:\D_Documents\ch3_Debugging_Exercises.docx",mode='r+b') as f:
	# data = f.read()
	# hashlib.sha256(data).hexdigest()