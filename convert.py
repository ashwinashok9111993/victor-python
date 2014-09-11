def con(n,b):
    d=[]
    while n>0:
        d.insert(0,n%b)
        n=n/b
    return d

def rev(digits,b):
    n=0
    for d in digits:
        n=b*n+d
    return n
