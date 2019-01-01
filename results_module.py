def results(inFile, alg, ckSum, k, status, verbosity):
    """
    Display the results of the program
    """
    baseMsg = (
              "\n --- Results for {0} ---\n"
              " Hash Algorithm:     {1}\n"
              " Checksum Generated: {2}\n"
              ) # end baseMsg
    
    extendedMsg = (
              " Verification Key:   {3}\n"
              " Validation Status:  {4!s}"
                  ) #end extendedMsg

    # Input file/ NO key, default output
    if k == '' and not verbosity :
        print(ckSum)

    # Input file/ NO key, VERBOSE output
    elif k == "" and verbosity :
        print(baseMsg.format(inFile, alg, ckSum))

    # Input file AND key, default output
    elif k != "" and not verbosity :
        print(status)

    # Input file AND key, VERBOSE output
    elif k != "" and verbosity :
        print((baseMsg + extendedMsg).format(inFile, alg, ckSum, k, status))

    # end results()