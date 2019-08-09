"""
This is a package in Python that will compute the results of numerical values provided.
A Calculator!
"""

print("Hi There! I have sum, diff, divide and multiply functionality")

""" To get the sum of two numbers """
def sum(n1, n2):
    return n1+n2

""" To get the difference of two numbers """	
def diff(n1, n2):
    return n1-n2
	
""" To get the multiplication of two numbers """
def multiply(n1, n2):
    return n1*n2
	
""" To get the division of two numbers """
def divide(n1, n2):
    if n2 != 0:
	    return n1/n2
    else:
	    return "Divide by zero is not possible!"