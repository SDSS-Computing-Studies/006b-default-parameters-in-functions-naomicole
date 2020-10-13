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


def toradians(angled):
    radians=(angled*math.pi)/180
    return radians

    
def solution(numbers):
    x2=numbers[1]
    return x2


def quadratic(a,b,c):
   m1= math.sqrt((b**2)-(4*a*c))
   m2= -b+m1
   x1=m2/(2*a)
   x1=round(x1,2)
   n1= math.sqrt((b**2)-(4*a*c))
   n2= -b-n1
   x2=n2/(2*a)
   x2=round(x2,2)
   lis=[]
   lis.append(x1)
   lis.append(x2)
   lis.sort
   return x1, x2
  

def cosineLaw(a,b,anglec, oppositeside="True"):
    sidec= math.sqrt(((a**2)+(b**2))+((-2*a*b)*(math.cos(anglec))))
    c=round(sidec,2)
    if oppositeside==False:
        if a>b:
            lnum=a
            snum=b

        elif b>a:
            lnum=b
            snum=a

        q1=1
        q2=2*snum*math.cos(toradians(anglec))
        q3=(snum**2)-(lnum**2)
        x=quadratic(q1,q2,q3)
        c=solutions(x)

    return c

