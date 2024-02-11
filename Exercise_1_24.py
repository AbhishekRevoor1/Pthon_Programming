"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

#This Programm Starts here [First Method]

""" def Vowel_Check(x):
    if x=="A" or x=="a":
        print("True")
    elif x=="E" or x=="e":
         print("True")
    elif x=="I" or x=="i":
         print("True")
    elif x=="O" or x=="o":
         print("True")
    elif x=="U" or x=="u":
         print("True")
    else:
         print("False")

Vowel_Check("e")
Vowel_Check("W")
Vowel_Check("O")
Vowel_Check("u")
Vowel_Check("b")
"""

# [Second Method]

def VowelCheck(x):
    AllVowels1="aeiou"
    AllVowels2="AEIOU"
    if x in AllVowels1 or x in AllVowels2:
       print("True")
    else:
       print("False")

VowelCheck("e")
VowelCheck("W")
VowelCheck("O")
VowelCheck("u")
VowelCheck("b")