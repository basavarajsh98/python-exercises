"""
Scope:
1) Write a function which takes two strings as arguments and checks if they're anagram fo each other
 - get the length of strings
 - check if they are of same length, if not then set the return value
 - sort the strings
 - compare each character of both the strings 
 - set the return value accordingly
2) Now, input two strings
3) call the function and print the output statements accordingly.
"""

def areAnagram(str1, str2):  
    # Get lengths of both strings  
    n1 = len(str1)  
    n2 = len(str2)   
    # If lenght of both strings is not same, then they cannot be anagram  
    if n1 != n2:  
        return 0 
    # Sort both strings  
    str1 = sorted(str1) 
    str2 = sorted(str2)  
    # Compare sorted strings  
    for i in range(0, n1):  
        if str1[i] != str2[i]:  
            return 0 
    return 1
  

# Driver program to test the above function  
str1 = input("First string: ")
str2 = input("Second string: ")
if areAnagram(str1, str2):  
    print ("The two strings are anagram of each other") 
else:  
    print ("The two strings are not anagram of each other") 