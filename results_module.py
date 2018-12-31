
def results(inFile, alg, k, ckSum, status, verbosity):
    """
    Display the results of the program
    """
    # Input file/ NO key, default output
    if k == '' and not verbosity :
        print(ckSum)

    # Input file/ NO key, VERBOSE output
    elif k == "" and verbosity :
        print('{0} {1} checksum: {2}'.format(inFile,alg,ckSum))

    # Input file AND key, default output
    elif k != "" and not verbosity :
        print(status)

    # Input file AND key, VERBOSE output
    elif k != "" and verbosity :

        msg = """{0} {1} Checksum:   {2}
              \rVerification Key:            {3}
              \rValidation Status:           {4!s}""".format(inFile, alg, ckSum, k, status)

        print(msg)

# End results()