def iseven(n1):
    if n1%2==0:
        return True
    return False
def isodd(n1):
    if n1%2!=0:
        return True
    return False
def isprime(n1):
#     c=0
    for i in range(2,n1):
        if n1%i==0:
            return False
    return True