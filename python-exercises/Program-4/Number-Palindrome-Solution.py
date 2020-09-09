#input a number
number=int(input("Enter a number:"))
#store the number in a temporary variable to make comparison
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