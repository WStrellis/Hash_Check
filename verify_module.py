
def verify(ckSum, k):
    """
    Compare the calculated checksum to the verification key
    """
    if ckSum == k:
        return True
    else:
        return False

# End verify()