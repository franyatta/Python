#Assignment 2 CS 115
#Francine Vo
#Student ID 01253035
num = int(input("Enter a number: "))
if (num % 2 == 0): #make sure to use == NOT =
  print(num, "is even")
else:
  print(num, "is odd")
if(num % 3 == 0):
  print(num, "is divisible by 3")
else:
  print(num, "is not divisible by 3")