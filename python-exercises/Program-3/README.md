# Exception

Andrew wants to teach how to open a file and write something in it to his son. Help him do this by writing a python program.

* If the file doesn't exists, it will throw IOError Exception. Catch it and print a message as
  "Error: can\'t find file or read data. Check the file access mode"

* When wrote something into the file successfully, it should print a message as
  "Written content in the file successfully"

* if cannpt write into the file, print a message as 
  "not writable. Check the file access mode"

* Whether written something into the file or not , it should close the file and print a message as
  "file closed".

**Use try, catch and finally to perform the above task.**

## Before you begin:

###### File Access Modes

* Read Only (‘r’) : Open text file for reading. 
                  If the file does not exists, raises I/O error. 
* Write Only (‘w’) : Open the file for writing. 
                   For existing file, the data is truncated and over-written. 
                   Creates the file if the file does not exists.
* Append Only (‘a’) : Open the file for writing. 
                    The file is created if it does not exist.
                    The data being written will be inserted at the end, after the existing data.

