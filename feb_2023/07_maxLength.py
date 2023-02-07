# Given an array arr[] consisting of n integers, 
# find the length of the longest subarray with positive (non zero) product.
def product(elem):
     curr = 1
     for i in elem:
       curr*=i
     return curr
def maxLength(self,arr,n):
  sub=[arr[j:i] for i in range(n+1) for j in range(i)]
  sub1=[len(i) for i in sub if product(i)>0]
  return max(sub1)
