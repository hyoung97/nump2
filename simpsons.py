def f(x): return 2*x/(1+x**2)
a=0
b=6

for k in range(1,4):
    n = 6*10**(k)
    h =(b-a)/n
    
    s=(f(a) +f(b))
    for i in range(1,n):
        if i%2==0:
            s=s+4*f(a+h*i)
        else:
            s=s+2*f(a+h*i)
    I  = (h/3)*s
    
    print(I)