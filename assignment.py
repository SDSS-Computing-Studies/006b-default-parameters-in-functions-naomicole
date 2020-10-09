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


def cosineLaw(sidea,sideb,anglec, by="True"):
    sidec=(sidea**2)+(sideb**2)-2*sidea*sideb*math.cos(anglec)
    c=math.sqrt(sidec)
    return c

def toradians():
    pass

def solution():
    pass

def quadratic():
    pass

x= cosineLaw(20,20,20)
print(x)