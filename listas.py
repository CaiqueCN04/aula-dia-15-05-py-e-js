a=float(input('coloque um numero: '))
b=float(input('coloque um numero: '))
c=float(input('coloque um numero: '))

i=-10
x=[]
y=[]

while i<10:
    x.append(i)
    f= a*i**2+b*i+c
    y.append(f)
    i+=1
    print(x)
    print(y)

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()