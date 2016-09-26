#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('100+200+300=',100+200+300)
print('1024 * 768 =', 1024*768)
print('''hello, world.
I\'m "OK"''')

def normalize(name):
    return name.capitalize()
L1 =['adam','LISA','braT']
L2 = list(map(normalize, L1))
print(L2)

print('The quick brown fox', 'jumps over', 'the lazy dog')
#name=input('please enter you name:')
#print('Hello,', name)
PI=3.1415926

print(3>2 and not True)
print(3>5 or True)
print(10//3)
print('Hello, %s, you have $%d' % ('Chet',1000))
print('%2d-%03d' % (3,1.5))
print('%.2f'% PI)
s1 = 72
s2 = 85
r = (s2-s1)/s2 *100
print('%.1f%%' % r)
print('中文'.encode('utf_8'))
print('中文'.encode('gb2312'))
classmate=['Michael','Bob','Tracy']
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[1])
print(classmate[2])
print(classmate[-1])
classmate.append('Adam')
classmate.insert(1,'Jack')
print(classmate)
print(classmate.pop())
print(classmate)
print(classmate.pop(1))
print(classmate)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print('%s. Length:%s' % (s,len(s)))
classmate=('Michael','Bob','Tracy')
print(classmate)

for name in classmate:
    print(name)
t=(1)
print(t)
t=(1,)
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
for item in L:
    for subitem in item:
        print(subitem)

age=14 #int(input('birth:'))
print('your age is %s' % age)
if age >=18:  
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')


def calcBMI(_height, _weight):
    bmi = _weight/(_height*_height)
    print('your bmi is %s', bmi)
    if bmi<=18.5:
        return 'too light'
    elif bmi<=25:
        return 'normal'
    elif bmi<=28:
        return 'too heavy'
    elif bmi<=32:
        return 'fat'
    else:
        return 'too fat'
height = 1.71
weight = 72
print(calcBMI(height,weight))

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
print(list(range(101)))
sum=0
for x in range(101):
    sum=sum+x
print(sum)
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)

n=1
while n<100:
    if n>10:
        break
    print(n)
    n=n+1
print('END')
n=0
while n<10:
    n=n+1
    if n%2 ==0:
        continue
    print(n)
d={'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Michael'])
d['Jack'] =90
print(d)
if 'Thomas' in d:
    print(True)
else:
    print(False)
print(d.get('Tracy'))
print(d.get('Non',-1))
print(d.pop('Bob'))
print(d)

s=set([1,2,3])
print(s)
s=set([1,1,2,3,2,3])
print(s)
s.add(4)
print(s)
s.remove(3)
print(s)
s2=set([4,5,2])
print(s & s2)
print(s | s2)

a =['c','b','a']
print(a)
a.sort()
print(a)
a = set((1,2,3))
print(a)
d= {'a':a}
print(d)

print(abs(-20))

n1=255
n2=1000
print(hex(n1))
print(hex(n2))

from functions import my_abs

print(my_abs(-100))
print(my_abs('1'))
print(my_abs('dd'))

import math
from functions import move
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r =  move(100, 100, 60, math.pi / 6)
print(r)
from functions import quadratic
print(quadratic(2,3,1))
print(quadratic(1,3,-4))

from functions import power
print(power(5))
print(power(5,2))
print(power(5,3))

from functions import add_end
print(add_end())
print(add_end())
print(add_end())

from functions import calc
print(calc(1,2,3))
print(calc(1,3,5,7))
print(calc())
print(calc(*[1,2,3]))

from functions import person
person('Michael',30)
person('Bob', 35, city='Bejing')
person('Adam', 45, gender ='M', job='Engineer')
person('Jack',24, **{'city':'Beijing', 'job': 'Engineer'})

from functions import f1
from functions import f2

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)
args=(1,2,3)
kw={'d':99, 'x':'#'}
f1(*args,**kw)
f2(*args,**kw)

from functions import fact
from functions import fact2
print(fact(1))
print(fact(5))
print(fact(100))

