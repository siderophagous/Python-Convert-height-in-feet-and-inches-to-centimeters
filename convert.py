##
#Python's program to convert height in feet and inches to centimeters.  
##
 
#Define the constants
CEN_IN_FEET = 12
CEN_IN_INCH = 2.54
 
 
#Read the input(height) from human
print("Enter your height:")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))
 
#Convert the input in equivaltent centimeters
centimeters = (feet * CEN_IN_FEET + inches) * CEN_IN_INCH
 
#Display the result
print("Your height in centimeters is:",centimeters)
