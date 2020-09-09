"""
Scope:
1) Input a number
2) Store it in a temporary variable to make comparison
3) Define and initialize a variable to store reversed number
4) Use while loop to:
 - extract the last digit from the number
 - reverse the digit position
 - redefine the number without the digit extracted in the current iteration.
5) Compare the reversed number and the input number
6) Print the output messages accordingly.
"""

#input a number
number=int(input("Enter a number:"))
#store the number in a temporary variable
temp=number
#initialse the variable which stores the reversed number 
reverse=0

#loop through until there are no digits in the number
while(number>0):
    #extract the last digit from the number
    digit=number%10
    #reverse the digit position
    reverse=reverse*10+digit
    #the number now becomes a digit less than it was before
    number=number//10

#compare the inputted number and it's reverse
if(temp==reverse):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

#Tip: Try to write a isPalindrome method