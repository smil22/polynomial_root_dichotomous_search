def horner(p,x):
    """
    This function evaluates a polynomial in a given value by using the horner method.
    - p: a list that contains the polynomial coefficients ranged in decreasing power order.
    - x: the value in which the polynomial must be evaluated.
    """
    y = p[0]
    n = len(p)
    for k in range(n-1):
        y = y*x + p[k+1]
    return y

def dichotomous_root(p,a,b,tol):
    """
    This function returns a root of the polynomial you give.
    - p: a list that contains the polynomial coefficients ranged in decreasing power order.
    - a,b: the boundaries of the research interval.
    - tol: a measure of the expected accuracy.
    """
    ya,yb = horner(p, a), horner(p, b)
    while ya * yb > 0:
        #extend research interval
        a -= b;
        b *= 2;
    if ya * yb == 0:
        if ya == 0:
            return a
        else:
            return b
    else:
        while abs(a-b) > tol:
            c = (a+b)/2
            yc = horner(p,c)
            if ya * yc < 0:
                b = c
                yb = horner(p,b)
            elif ya * yc == 0:
                if ya == 0:
                    return a
                else:
                    return c
            else:
                a = c
                ya = horner(p,a)
    return (a+b)/2
