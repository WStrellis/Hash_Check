
def verify(ckSum, k):
    """
    Compare the calculated checksum to the verification key
    """
    if ckSum.lower() == k.lower():
        return True
    else:
        return False

    # End verify()