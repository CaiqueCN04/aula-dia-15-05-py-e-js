a=float(input('coloque um numero: '))
b=float(input('coloque um numero: '))
c=float(input('coloque um numero: '))

delta=b**2-4*a*c

if delta<0:
    print('não tem raiz')
elif delta==0:
    x=-b/(2*a)
    print(f'ambas as raizes são iguais a {x}')
else:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print(f'a primeira raiz vale {x1} e a segunda vale {x2}')

xv=-b/(2*a)
yv=-delta/(4*a)
print(f'o vertice esta em {xv} e {yv}')

