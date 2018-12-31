##Program Name
---
Hash Check

##Lanuages Used:
---
Python 3.7

##Program Description:
---
A program that generates checksums of a file. It also accepts a key as an input. If a key is entered the checksum will be compared to the key.

##Program Outline:
---

1. Start the Main() function.
2. Analyze command line input using argparse.
3. Call getAlg() from hash_module.py to set the hash algorithm for calcChecksum().
4. Call calcChecksum() from hash_module.py to calculate the checksum for the input file. Store the result in variable called “checkSum”.
5. Call verify() from the verify_module.py. Store the result in the “valid” variable.
6. If a checksum was successfully generated call the results() function from results_module.py to display the results of the program.

