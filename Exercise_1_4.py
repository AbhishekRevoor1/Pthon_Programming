""" Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504 """

# This program starts here
import math
r=float(input("Enter radius of the circle"))
Area=(math.pi) * r * r
print(f"r = {r}")
print(f"Area = {Area}")