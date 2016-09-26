def my_abs(x):
    if not isinstance(x,(int,float)):
        #raise TypeError('Bad operand type.')
        print('Bad operand type.')
        return
    if x>=0:
        return x
    if x<0:
        return -x

import math
def move(x,y,step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) and 
        isinstance(b, (int, float)) and
        isinstance(c, (int,float))):
        print("Bad Parameter(s).")
    d = b ** 2 - 4 * a * c
    if d<0:
        print('no valid result.')
    elif d==0:
        print('only one result')
        return -b/(2*a)
    else:
        print('there are two results')
        ans1 = (-b + d ** 0.5)/(2 * a)
        ans2 = (-b - math.sqrt(d))/(2 * a)
        return (ans1,ans2)

def power(x, n=2):
    s=1
    while n >0:
        n=n-1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def calc(*numbers):
    sum = 0 
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name: %s age: %s other: %s' % (name,age,kw))

def person2(name,age, *, city,job):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name: %s age: %s other: %s' % (name,age,kw))

def f1(a,b,c=0, *args, **kw):
    print('a=%s b=%s c=%s args=%s kw=%s' % (a,b,c,args,kw))
def f2(a,b,c=0,*,d,**kw):
    print('a=%s b=%s c=%s d=%s kw=%s' % (a,b,c,d,kw))

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
#尾递归调用, python并没有针对此进行优化
def fact2(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num==1:
        return product
    return fact_iter(num-1, num* product)


