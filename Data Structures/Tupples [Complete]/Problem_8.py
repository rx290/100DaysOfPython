"""
Write a Python program to print a tuple with string formatting. 
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)
""" 
t = (100, 200, 300)
print("This is a tuple",t)
print("This is a tuple {argument}.".format(argument = t))
