# Given a linked list of characters and a string S.
# Return all the anagrams of the string present in the given linked list.
# In case of overlapping anagrams choose the first anagram from left.
#User function Template for python3
from collections import Counter,defaultdict
class Solution:
    def findAnagrams(self, head, s):
        n = len(s)
        s = Counter(s)
        ans = list()
        while head:
            d = defaultdict(int)
            x = head
            i = 0
            l = Linked_List()
            while x and i < n:
                l.insert(x.data)
                d[x.data] += 1
                x = x.next
                i += 1
            if d == s:
                head = x
                ans.append(l.head)
            else:
                head = head.next
        
        return ans
                
                
        # code here
