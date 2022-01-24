# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:03:02 2022

@author: Khalid Ayub Ansari
"""

#step function in for loop
for x in range(0,12,2):
    print(x)
    
# to make a for loop infinite
#yes,a for loop can be infinite.
def infinity():
    while True:
        yield
for _ in infinity():
    pass

# how to add values in a tuple'
#tuples are immutable but adding a value to a tuple results in a new tuple with
#a new value added at the end of it. use the + value to add a value to a tuple
a_tuple=("h","i")
added_value="j"
added_value_tuple=(added_value,)
new_tuple= a_tuple+added_value_tuple
print(new_tuple)


