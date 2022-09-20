#Assignment 1

import math


##Question 1

fruits = ["apple", "banana", "cranberry", "date", "eggplant", "fennel", "guava"]
print (fruits)
big = []
small = []
for fruits in fruits:
#    print (fruits)
    n = (len(fruits))
    if n > 5:
        big.append(fruits)
    else:
        small.append(fruits)
print ("Greater than 5 letters = ")
for big in big:
    print(big)
print ("smaller or equal to 5 letters = ")
for small in small:
    print(small)
print("done")
    
    
####################################

## Question 2
def TF (x):
    number = x
    number = int(number)
    if number > 0:
        return True
    else:
        return False
    return 

#TF ()

a = int(input("a of the quadratic eqn"))
b = int(input("'b' of the quadratic eqn"))
c = int(input("'c' of the quadratic eqn"))

def quadraroots ( a, b, c):
    d = (b * b) - (4 * a * c)
    root1 = int((-b - math.sqrt(d))/(2*a))
    root2 = int((-b + math.sqrt(d))/(2*a))
    print("The roots are ",root1,root2)
    sign1 = TF(root1)
    
    sign2 = TF(root2)
    if sign1 == sign2:
        print("The roots are of the same sign")
    else:
        print("The roots are of different signs")
    
quadraroots (a, b, c)
	
#################




