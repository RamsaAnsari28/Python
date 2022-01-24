# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 19:33:34 2022

@author: Khalid Ayub Ansari
"""

#methods of list
list=[1,4,5.2,"red"]
list.append("blue")


list.clear()

list.copy()

list1=["green,orange,yellow"]
list1.count("orange")
list.extend(list1)

list1.index("yellow")

list1.insert(1, "black")

list1.pop(3)

list.remove("red")
 
list.reverse()

list1.sort()

#methods of strings

text="hello everyone and welcome to my channel."
x=text.capitalize()

x=text.casefold()

x=text.center(10)

text1="i love winter,winter is the best"
x=text1.count("winter")

x=text.encode()

x=text.endswith(".")

x=text.find("welcome")

#usage of negative numbers as index,it is used to display data from the end of
the list, that means it starts from where the arrays end.