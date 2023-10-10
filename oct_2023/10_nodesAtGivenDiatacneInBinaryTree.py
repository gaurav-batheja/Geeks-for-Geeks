# Given a binary tree, a target node in the binary tree, and an integer value k, find all the nodes that are at distance k from the given target node. No parent pointers are available.
# Note:

# You have to return the list in sorted order.
# The tree will not contain duplicate values

#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def KDistanceNodes(self,root,target,k):
        ans=[]
        
        #case_1
        
        def subtree(root,k):
            if k<0 or root==None:
                return 
            
            if k==0:
                ans.append(root.data)
                return
                
            subtree(root.left,k-1)
            subtree(root.right,k-1)
        
        #case2
        
        def anc(root, dis):
            if root==None:
                return -1
            
            if root.data==target:
                subtree(root,k)
                return 0
            
            left=anc(root.left,dis)
            
            if left!=-1:
                if left+1==k:
                    ans.append(root.data)
                else:
                    subtree(root.right,k-left-2)
                return left+1
            
            right=anc(root.right,dis)
            
            if right!=-1:
                if right+1==k:
                    ans.append(root.data)
                else:
                    subtree(root.left,k-right-2)
                return right+1
            
            return -1
        
        anc(root,k)
        ans.sort()
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends
