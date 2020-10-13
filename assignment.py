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


def toRadians(angled):
    radians=(angled*math.pi)/180
    return radians

    
def solution(numbers):
    x2=numbers[1]
    return x2


def quadratic(a,b,c):
   m1= math.sqrt((b**2)-(4*a*c))
   m2= (-1*b)+m1
   x1=m2/(2*a)
   n1= math.sqrt((b**2)-(4*a*c))
   n2= (-1*b)-n1
   x2=n2/(2*a)
   lis=[]
   lis.append(x1)
   lis.append(x2)
   lis.sort()
   return lis
  

def cosineLaw(a,b,anglec, oppositeSide=True):
    sidec= math.sqrt(((a**2)+(b**2))+((-2*a*b)*(math.cos(toRadians(anglec)))))
    c=sidec
    if oppositeSide==False:
        if a>b:
            lnum=a
            snum=b

        elif b>a:
            lnum=b
            snum=a

        q1=1
        q2=(-1*2)*snum*math.cos(toRadians(anglec))
        q3=(snum**2)-(lnum**2)
        x=quadratic(q1,q2,q3)
        c=solution(x)

    return c

