import math

def isprime(N):
    """素数ならTrue, そうでなければFalseを返す"""
    
    flg=True
    for i in range(2,N):
        if (N%i)==0:
            flg=False
            break
    
    return flg