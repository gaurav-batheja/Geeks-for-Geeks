# Bob is very fond of balloons. Once he visited an amusement park with his mother. 
# The mother told Bob that she would buy him a balloon only if he answer her problem right.
# She gave Bob a string S [contains only lowercase characters] and asked him to use the characters of string to form as many instances of the word "balloon" as possible.
# Return the maximum number of instances that can be formed.
# Help Bob to solve the problem.
# Note: You can use each character in the string at most once.

def maxInstance(self, s : str) -> int:
        b,a,l,o,n=0,0,0,0,0
        for i in s:
            if i=='b':
                b+=1
            elif i=='a':
                a+=1
            elif i=='l':
                l+=1
            elif i=='o':
                o+=1
            elif i=='n':
                n+=1
        l,o=l//2,o//2
        return min(b,a,l,o,n)
