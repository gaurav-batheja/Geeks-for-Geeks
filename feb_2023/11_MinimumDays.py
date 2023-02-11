# Given a string S of length N containing only lowercase alphabets. You are also given a permutation P of length N containing integers from 0 to N-1.
# In (i+1)'th day you can take the P[i] value of the permutation array and replace S[P[i]] with a '?'.

def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
    S,day=list(S),0
    for i in P:
        if i<len(S)-1 and  S[i]==S[i+1]:
            day=P.index(i)+1
        elif i!=0 and S[i]==S[i-1]:
            day=P.index(i)+1
    return day
