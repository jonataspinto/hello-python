def subTwo(a,b):
    return (a-b)**2
import math

def sumTwo(n1,n2):
    return (n1+n2)**2

def function1():
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))

    d = math.sqrt(
        (subTwo(x1,y1) + subTwo(x2,y2))
    )

    print(d)

def function2():
    a = int(input('value 1: '))
    b = int(input('value 2: '))    
    c = int(input('value 3: '))
    val1 = sumTwo(a,b)
    val2 = sumTwo(b,c)
    result = (val1 + val2) / 2
    print(result)


