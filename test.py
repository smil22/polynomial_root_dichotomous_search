import library

p = [4,0,-6,2] #p(x) = 4x³-6x+2
a,b,tol = -2,0,1e-5
ya = horner(a)
yb = horner(b)
print(ya,yb)
