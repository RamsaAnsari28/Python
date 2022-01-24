# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:23:04 2022

@author: Khalid Ayub Ansari
"""

#methods of dictionary
flower={"rose,lily,lotus,tulip"}
flower.clear()

x= flower.copy()

x=('red1','red2','red3')
y=0
thisdict=dict.fromkeys(x,y)

fashion={'brand':'nykaa','model':'lipstick'}
x=fashion.get("brand")

x=fashion.items()

x=fashion.keys()

x=fashion.pop("model")

x=fashion.popitem()

x=fashion.setdefault('color','pink')

fashion={"year":"2021","month":"january"}
y=fashion.values()

#create a set

thisset={"rahul,raj,shyam,rohan"}
print(thisset)

#most frequent character 
c=[2,4,6,1,3,8,7]
c.sort(reverse=True)
print(c)

#filename extension

filename=input("enter filename:")
filename=filename.split(".")
print("extension of the file is;"+filename(-1))

#calculator using if conditions and functions

print("1 Add")
print("2 sub")

choice = input("enter your choice: ")

num1= float(input("enter number 1: "))
num2= float(input("enter number 2:"))

if choice =="1":
    print(num1,"+", num2,"=",(num1+num2))





