"""
Scope:
1) Write a function which takes the side lengths and the angle to determine the shape
 - Make use of if, elif and else statements to set the conditions for shape
 - print the shape message accordingly
2) Input all the four sides of a shape and an internal angle 
3) Convert the input values to float
4) Make the function call with converted side lengths and angle as the arguments.
"""

# Function to determine what shape does the sides and angle make
def get_shape(s1,s2,s3,s4,angle):
    if( ((s1+s2+s3+s4)/4 == s1) & (angle == 90)):
        print("It's a square")
    elif ( (s1 == s3) & (s2 == s4) & (angle == 90) ): 
        print("It's a rectangle")
    elif ( ((s1+s2+s3+s4)/4 == s1) & (angle != 90) ):
        print("It's a rhombus")
    elif ( (s1 == s3) & (s2 == s4) & (angle != 90) ): 
        print("It's a parallelogram")
    else:
        print("It's a irregular quadrilateral")

# Driver program to test the above function  

#input the length of the sides
side1 = float(input("Enter the length of first side in cm: "))
side2 = float(input("Enter the length of second side in cm: "))
side3 = float(input("Enter the length of third side in cm: "))
side4 = float(input("Enter the length of fourth side in cm: "))
#input any internal angle
angle = float(input("Enter one internal angle: "))
#method call
get_shape(side1,side2,side3,side4,angle)

#Tip: Try to input all the sides lengths in a single statement
# sides = [float(side_length) for side_length in input("Enter the length of the four sides in cm: ").split(",")] 
# side1 = sides[0]
# side2 = sides[1]
# side3 = sides[2]
# side4 = sides[3]