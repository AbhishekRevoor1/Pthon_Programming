"""
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

"""

#This program Starts here
def calculate(a,b,c):
    sum=a+b+c
    if a==b==c:
        return sum*3
    else:
        return sum
    
print(calculate(2,5,7))
print(calculate(2,2,2))    
