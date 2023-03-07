# You are given a tree rooted at node 1.
# The tree is given in form of an array P where Pi denotes the parent of node i,
# Also P1 = -1, as node 1 is the root node. Every node i has a value Ai associated with it. 
# At first, you have to choose any node to start with, after that from a node you can go to any of its child nodes. 
# You've to keep moving to a child node until you reach a leaf node. Every time you get to a new node,
# you write its value. Let us assume that the integer sequence in your path is B.
# Let us define a function f over B, which is defined as follows:
# f(B) = B1 - B2 + B3 - B4 + B5.... + (-1)(k-1)Bk.
# You have to find the maximum possible value of f(B).
def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
    # code here
    def _solve(ix):            
        if cs[ix]:
            for c in cs[ix]: _solve(c)
            dp[ix] = max( A[ix] - A[i] + cmax[i] for i in cs[ix] )
            cmax[ix] = max( dp[i] for i in cs[ix] )
        else:
            dp[ix] = A[ix]
            cmax[ix] = 0

    cs = [[] for _ in range(N)]
    dp, cmax = [0] * N, [0] * N
    for i in range(1, N): cs[P[i]-1].append(i)
    _solve(0)
    return max(dp)
