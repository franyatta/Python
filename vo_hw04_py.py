#Assignment 3 for Francine Vo
#Student ID 01253035
num1 = input('Input the first number: ')
num2 = input('Input the second number: ')
num3 = input('Input the third number: ')
num4 = input('Input the fourth number: ')
#Use nested branching statements to determine the highest number
#NO LOOPS
if num1 >= num2 and num1 >= num3 and num1 >= num4:
  greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
else:
  greatest = num4
print("The greatest number is", greatest)