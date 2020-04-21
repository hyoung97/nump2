%https://www.math.tamu.edu/~phoward/m289/riemann.pdf

%Left Riemman Sum

function value=rsum1(f,a,b,n)
%RSUM1: Computes a Riemann Sum for the function f on
%the interval [a,b] with a regular partition of n points.
%The points on the intervals are chosen as the right endpoints.

value = 0;
dx = (b-a)/n;
for k=0:n-1
c = a+k*dx;
value = value + f(c);
end
value = dx*value;