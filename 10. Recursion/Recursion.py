def fib_rec(a):
    if a<=1:
        return a
    else: 
        return fib_rec(a-2)+fib_rec(a-1)
    
    
    
def fib_iter(n):
    a=0
    b=1
    if n<=1:
        return n
    
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
    
def fib_dp(n):
    f=[0,1]
    
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
        

import time
if __name__=='__main__':
    
    start=time.time()
    print(fib_rec(25))
    end=time.time()
    print('recursive',(end-start)*1000)

    start=time.time()
    print(fib_iter(25))
    end=time.time()
    print('iterative',(end-start)*1000)
    
    start=time.time()
    print(fib_dp(25))
    end=time.time()
    print('DP',(end-start)*1000)
