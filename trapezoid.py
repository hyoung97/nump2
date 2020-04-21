#https://www.google.com/search?q=trapezoidal+rule+matlab&oq=trapezoid+rule+matla&aqs=chrome.1.69i57j0l7.8247j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_w1eXXuTuHsivggeC7p34CQ48
def f(x): return 2*x/(1+x**2)
a=0
b=6

for k in range(1,4):
    n = 6*10**(k)
    h =(b-a)/n
    
    s=0.5*(f(a) +f(b))
    for i in range(1,n):
        s=s+f(a+h*i)
    I  = h*s
    
    print(I)