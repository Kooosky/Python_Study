import math

def isprime(N):
    """素数ならTrue, そうでなければFalseを返す"""
    
    mxdv=math.floor(math.sqrt(N))
    flg=True
    for i in range(2,mxdv+1):
        if (N%i)==0:
            flg=False
            break
    
    return flg