import library

p = [4,0,-6,2] #p(x) = 4x³-6x+2
a,b,tol = -2,0,1e-5

root = library.dichotomous_root(p, a, b, tol)

print('Root: {0:3.4f}\tEvaluation: {1:3.4e}'.format(root,library.horner(p,root)))
