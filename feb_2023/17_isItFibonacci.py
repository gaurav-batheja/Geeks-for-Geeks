# Geek just learned about Fibonacci numbers.

# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
# where the next number is found by adding up the two numbers before it.

# He defines a new series called Geeky numbers. Here the next number is the sum of the K preceding numbers.
# You are given an array of size K, GeekNum[ ], where the ith element of the array represents the ith Geeky number. Return its Nth term.

# Note: This problem can be solved in O(N2) time complexity but the user has to solve this in O(N). 
# The Constraints are less because there can be integer overflow in the terms.
def solve(self, N, K, GeekNum):
    z=0
    GeekNum+=[0 for i in range(N-len(GeekNum))]
    for i in range(K,N):
        for j in range(1,K+1):
            z+=GeekNum[i-j]
        GeekNum[i]=z
        z=0
    return GeekNum[N-1]
