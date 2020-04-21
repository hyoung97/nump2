import math

def func(x):
    return (x/(1+x**2))
def deq( x, y ): 
	return (1/(1+x**2)-2*y**2) 
	
# Function for euler formula 
def euler( x0, y, h, x ): 
	temp = -0
	maxerr=0

	# Iterating till the point at which we 
	# need approximation 
	while x0 < x: 
		temp = y 
		y =y+0.5*h*(deq(x0,y)+deq(x0+h,y+h*deq(x0,y)))
		x0=x0+h
		yact = func(x0)
		err=abs((yact-y)/y)*100
		if err>maxerr:
		    maxerr=err

	# Printing approximation 
	print("Approximate solution at x = ", x, " is ", "%.6f"% y) 
	print("Error: ", maxerr, "%")
# Driver Code 
# Initial Values 
x0 = 0
y0 = 0
h = 0.001

# Value of x at which we need approximation 
x = 10

euler(x0, y0, h, x) 
