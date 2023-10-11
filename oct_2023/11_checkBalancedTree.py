# Given a binary tree, find if it is height balanced or not. 
# A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree.

class Solution:
    def isBalanced(self,root):
    
        #add code here
        def traverse(root):
            nonlocal flag
            if not root: return 0
            lh=traverse(root.left)
            rh=traverse(root.right)
            if abs(lh-rh)>1: flag=0
            return max(lh,rh)+1
        flag=1
        traverse(root)
        return flag
