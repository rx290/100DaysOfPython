"""
If the ages of Mark, David, and Tom are input by the user, write a program to determine the youngest of the three.
"""

mark_age = int(input("Hey Mark, Please enter your age: "))
david_age = int(input("Hey David, Please enter your age: "))
tom_age = int(input("Hey Tom, Please enter your age: "))

ages = {mark_age:"Mark",david_age:"David",tom_age:"Tom"}

print("The youngest one is: {}".format(ages[min(ages)]))