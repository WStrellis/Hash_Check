
def results(inFile, alg, k, ckSum, status):
    """
    Display the results of the program
    """
    verbose = '{0!s} {1!s} checksum: {2!s}'.format(inFile,alg,ckSum)
    print(verbose)

# End results()