# Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

class Solution:
    def romanToDecimal(self, S): 
        d={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if len(S)==1:
            return d[S]
        L=[d[x] for x in S]
        for i in range(len(L)-1):
            if L[i]<L[i+1]:
                L[i]=L[i]*-1
        return sum(L)
