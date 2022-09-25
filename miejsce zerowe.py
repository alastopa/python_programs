def f(x):
    return x**3+0.3*x**2+0.5*x-5

a=-5
b=5

dokladnosc=0.00001

if f(a)*f(b)>0:
    print("Wartości funkcji na koncach przdziału są tego samego znaku. Podaj inne a i b")
    quit()

iteracja = 0
while abs(a-b)>dokladnosc:
    iteracja = iteracja + 1
    c=(a+b)/2
    if f(a)*f(c)<0:
        b=c
    elif f(a)*f(c)==0:
        a=c
        b=c
    else:
        a=c
    print("iteracja:", iteracja, "dlugosc przedzialu = ", abs(a-b))

wynik=(a+b)/2
print("miejsce zerowe = ", wynik)