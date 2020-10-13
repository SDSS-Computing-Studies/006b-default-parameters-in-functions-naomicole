#! python3

import math

def tempConversion(a, by="C"):
    f=((a*(9/5))+32)
    y=f
    answer=y
    if by=="F":
        c=(a-32)*(5/9)
        y=c
        answer=y

    answer=round(y,1)
    return answer

def factorPair(a,b):
    c=a/b

    fList=[int(b),int(c)]
    fList.sort()
    answer=fList

    return answer


def cosineLaw(a,b,anglec, by="True"):
    sidec= math.sqrt(((a**2)+(b**2))+((-2*a*b)*(math.cos(anglec))))
    return sidec


def toradians(angled):
    radians=(angled*math.pi)/180
    return radians

    

def solution():
    pass

def quadratic():
    pass

x= toradians(37)
print(x)

y= cosineLaw(11,8,x)
print(y)