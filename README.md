## Program Name  

Hash Check

## Language:  

Python 3.7

### Dependencies:

None

## Program Description:  

A program that generates checksums of a file. It also accepts a key as an input. If a key is entered the checksum will be compared to the key.

Example:

```
 C:\Users\wstre>hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso" --algorithm md5 --key 1F67BB3BD062DC754A35E2C7FA8414E9 -v

 --- Results for linuxmint-19-cinnamon-64bit-v2.iso ---
 Hash Algorithm:     md5
 Checksum Generated: 1F67BB3BD062DC754A35E2C7FA8414E9
 Verification Key:   1F67BB3BD062DC754A35E2C7FA8414E9
 Validation Status:  True
 ```

## Windows Setup  

This is section describes how to add hash_check_win.py to your system path so that you can run it from any directory without entering the full path to the file.  

`hash_check someFile.exe`

is much easier to type than: 

 `python C:/users/joe/python/scripts/hash_check_win.py someFile.exe`

1. Fork this repository onto your local machine. Example file structure:
    C:/Users/YourName/hash_check/theFilesForThisProgram

2. Create a batch file using a text editor. Save it as "hash_check.bat" and save in a folder for batch files.  

    It only needs this one line:    

    @py.exe full\path\to\hash_check_win.py %*     

    *The name of the .bat file is what you will use to invoke the program on the command line!*

    If you name the file "potatoes.bat" and it has the above line of code, then you would run hash_check_win.py in a terminal by typing:  

    `potatoes someFile.exe`    

3. Press the Windows Key + R to open the "Run" prompt. Enter the following command:  

    systempropertiesadvanced.exe  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step1.jpg "Open Run prompt")

    Alternatively, press the Windows Key + Pause Key to open the System window and then click "Advanced System Settings" on the left side.  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step1b.png "Open System Settings")  

4. Click "Environment Variables".  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step2.png "Open Environment Variables")  

5.  Within the "Environment Variables" window, click on the row with the variable "Path" under the "System Variables" section. You may also select "Path" under "User Variables for X" but the changes made will only effect that user.  

    After clicking on one of the rows with the "Path" variable click "Edit".  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step3.png "Select Path and click Edit")  

6. This will bring up a new window with a list of directories that are on the selected "Path"( either "System" or "User").  

    Click "New" and then enter the full path to the directory in which you store your .bat files.  

    Example:  C:\Users\YourName\my_batch_files\     

    You do not need to enter file names. The "Path" variable is a list of directories the computer will search for a file when the file is not found in the current working directory.  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step4.png "Add the .bat folder to your system path")    

    Then click "OK" on all of the system settings windows.

7. Open a command terminal by pressing Windows Key + R and then typing "cmd". Click "OK" or press Enter. This will open a terminal session.  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step5.jpg "Open a terminal session")    

8. Type "hash_check" or whatever you named the .bat file for this program and press enter. It should execute hash_check_win.py and display this output:  

    ![alt text](https://s3.amazonaws.com/staranen-images-001/step6.jpg "Test the changes")    

    If you get the output:  
    `'hash_check' is not recognized as an internal or external command, operable program or batch file.`  
    go back and check the environment variables and path settings.


## Usage:

Arguments do not need to be placed in any particular order.

` hash_check --key ge35fs234 -v "some_file.x" -a sha512`

is the same as

` hash_check "some_file.x" --k ge35fs234 -a sha512 -v`

### Required Arguments  

**File**  

 The absolute or relative path to a file that you would like to process. Wrap the file in quotes:  

`hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso"`

### Optional Arguments

**Help**  

```
 hash_check -h
 hash_check --help  
 ```

Show the help message.

**Algorithm**  

```
hash_check "some_file.x" -a md5  
hash_check "some_file.x" --algorithm md5
```  

The algorithm used to generate a checksum. Lowercase characters only. If unspecified, the default algorithm is sha256.

Algorithms Available:  

* md5
* sha1
* sha224
* sha256
* sha384
* sha512
* blake2b
* blake2s

**Key**  

` hash_check "some_file.x" -k 4G5434GV54234DFHE`   

A key used to verify the integrity of the input file. Case insensitive.

**Buffer Size**

` hash_check "some_file.x" -b 1024`  

The buffer size used to read the input file. If unspecified, the system's default buffer size will be used.  

**Verbose Output**

` hash_check "some_file.x" -v`  

Enable more detailed output messages.

**Examples**

Only specifying an input file:

```
C:\Users\wstre>hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso"
C92A9BAAFDD599DA057A97236F0A853CE1F8B3C7AD41E652CEBA493F9CA5623F
```

Input file with Verbosity enabled:

```
C:\Users\wstre>hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso" -v

 --- Results for linuxmint-19-cinnamon-64bit-v2.iso ---
 Hash Algorithm:     sha256
 Checksum Generated: C92A9BAAFDD599DA057A97236F0A853CE1F8B3C7AD41E652CEBA493F9CA5623F
 ```

 Changing the hash algorithm:

 ```
 C:\Users\wstre>hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso" -a md5 -v

 --- Results for linuxmint-19-cinnamon-64bit-v2.iso ---
 Hash Algorithm:     md5
 Checksum Generated: 1F67BB3BD062DC754A35E2C7FA8414E9
 ```

 Validating a file by including a verification key with default output:  

 ```
 C:\Users\wstre>hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso" -a md5 -k 1F67BB3BD062DC754A35E2C7FA8414E9 
 True
 ```  

 Validating a file by including a verification key with verbosity:

 ```
 C:\Users\wstre>hash_check "D:\Downloads\linuxmint-19-cinnamon-64bit-v2.iso" -a md5 -k 1F67BB3BD062DC754A35E2C7FA8414E9 -v

 --- Results for linuxmint-19-cinnamon-64bit-v2.iso ---
 Hash Algorithm:     md5
 Checksum Generated: 1F67BB3BD062DC754A35E2C7FA8414E9
 Verification Key:   1F67BB3BD062DC754A35E2C7FA8414E9
 Validation Status:  True
 ```

## Program Outline:

1. Start the Main() function.
2. Analyze command line input using argparse.
3. Call getAlg() from hash_module.py to set the hash algorithm for calcChecksum().
4. Call calcChecksum() from hash_module.py to calculate the checksum for the input file. Store the result in variable called “checkSum”.
5. Call verify() from the verify_module.py. Store the result in the “valid” variable.
6. If a checksum was successfully generated call the results() function from results_module.py to display the results of the program.

