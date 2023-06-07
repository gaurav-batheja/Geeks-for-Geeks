# Given a number N, find the least prime factors for all numbers from 1 to N.  The least prime factor of an integer X is the smallest prime number that divides it.
# Note :
# 1 needs to be printed for 1.
# You need to return an array/vector/list of size N+1 and need to use 1-based indexing to store the answer for each number.
def leastPrimeFactor(N):
    l,prime,k=[0,1,2,3],[2,3],4
    for i in range(4,N+1):
        appn=False
        for j in prime:
            if k%j==0:
                l.append(j)
                k,appn=k+1,True
                break
        if not appn:
          l.append(k)
          prime.append(k)
          k+=1
    return(l)
