"""
Scope:
1) Begin with a try block
2) Write the code to open a file
3) Next, write a catch block
4) Print a message to display when the file cannot be opened inside the catch block.
5) Use another try-except block inside the main try block
6) Try to write something into the opened file and print the success message
7) Catch the error if cannot write into the file and print the failure message
8) Make use of finally block to close the file regardless of writting into the file 
"""

try:
    #if file exists, then this block executes
    fileptr = open("file.txt","r") 
    #if opened   
    try:    
        #then write something into it
        fileptr.write("Hi I am good")
        print("Written content in the file successfully")
    except:
        #if cannot be written, then this block is executed.
        print("not writable.")    
    finally: 
        #close the file regardless of whether you write something into it or not   
        fileptr.close()    
        print("file closed")    
except IOError:  
    #if file doesn't exists, then this block is executed
    print("Error: can\'t find file or read data. Check the file access mode")