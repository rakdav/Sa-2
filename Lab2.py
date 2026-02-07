# a=float(input("Введите a:"))
# b=float(input("Введите b:"))
# if a>b: print(a,">",b)
# elif a<b: print(a,"<",b)
# else: print(a,"=",b)

# from math import *
#
# a=float(input("Введите a:"))
# b=float(input("Введите b:"))
# c=float(input("Введите c:"))
# D=b**2-4*a*c
# if D>0:
#     x1=(-b+sqrt(D))/(2*a)
#     x2=(-b-sqrt(D))/(2*a)
#     print("x1={:7.2f}".format(x1),"x2={:7.2f}".format(x2))
# elif D==0:
#     x=-b/(2*a)
#     print("x={:7.2f}".format(x))
# else: print("Корней нет")

# n=int(input("Введите номер месяца:"))
# if n==12 or n==1 or n==2:print("Зима")
# elif n==3 or n==4 or n==5:print("Весна")
# elif n==6 or n==7 or n==8:print("Лето")
# else: print("Осень")

from math import *

# x=float(input("Введите x:"))
# y=float(input("Введите y:"))
# print((x**2+y**2)<=4)
# print((x>=0) or (y!=4))
# print((x<=0) and (y!=4))
# print((x*y!=0) and (y>x))
# print((x*y!=0) or (y<x))
# print(not (x*y<0) and (y>x))
# print(not (x*y<0) or (y>x))
# print((x**2-y**2)<=0)

# a=float(input("Enter a number a: "))
# S=a**2
# b=sqrt(S/2)
# print("{:7.2f}".format(sqrt(S/b**2)))

# from math import sqrt
# a = float(input("введите число"))
# h = float(input("введите число"))
# b = float(input("введите число"))
# s1 = a**2
# s2 = b**2
# v = h*(s1 + sqrt(s1*s2) + s2) / 3
# print("v=","{:7.2f}".format(v))

import math

#Средний уровень 5 вариант
from math import *
t=float(input("Введите t:"))
p=3
k=sqrt(p*t)
x=p*t**2+sqrt(k)
y=tan(x**2)**3+k*t
print("y=","{:7.2f}".format(y))