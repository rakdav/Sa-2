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

x=float(input("Введите x:"))
y=float(input("Введите y:"))
print((x**2+y**2)<=4)
print((x>=0) or (y!=4))
print((x<=0) and (y!=4))
print((x*y!=0) and (y>x))
print((x*y!=0) or (y<x))
print(not (x*y<0) and (y>x))
print(not (x*y<0) or (y>x))
print((x**2-y**2)<=0)