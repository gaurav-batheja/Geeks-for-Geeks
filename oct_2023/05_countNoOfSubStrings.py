# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters.
class Solution:
    def substrCount (self,s, k):
        n=len(s)
        def solve(k):
            i,j=0,0
            ans=0
            c=0
            d={}
            while j<n:
                if s[j] not in d:
                    d[s[j]]=1
                    c+=1
                else:
                    d[s[j]]+=1
                while c>k:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        d.pop(s[i])
                        c-=1
                    i+=1
                ans+=j-i+1
                j+=1
            return ans
        return solve(k)-solve(k-1)
