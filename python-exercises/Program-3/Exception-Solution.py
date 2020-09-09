# File Access Modes
# Read Only (‘r’) : Open text file for reading. 
#                   If the file does not exists, raises I/O error. 
# Write Only (‘w’) : Open the file for writing. 
#                    For existing file, the data is truncated and over-written. 
#                    Creates the file if the file does not exists.
# Append Only (‘a’) : Open the file for writing. 
#                     The file is created if it does not exist.
#                     The data being written will be inserted at the end, after the existing data.

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