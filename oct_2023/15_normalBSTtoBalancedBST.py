# Given a Binary Search Tree, modify the given BST such that it is balanced and has minimum possible height. Return the balanced BST.


class Solution:
    def construct(self, res, root, low, high, left):

        mid = (low+high)//2
        if low<high and root:
            if left:
                root.left = res[mid]
                self.construct(res, root.left, low, mid-1, True)
                self.construct(res, root.left, mid+1, high, False)
            else:
                root.right = res[mid]
                self.construct(res, root.right, low, mid-1, True)
                self.construct(res, root.right, mid+1, high, False)
        elif low==high and root:
            if left:
                root.left = res[mid]
            else:
                root.right = res[mid]
            res[mid].left = None
            res[mid].right = None
        else:
            root.left = None
            root.right = None
        
    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root)
        self.inorder(root.right, res)
            
    def buildBalancedTree(self,root):
        #code here
        if root:
            res = []
            self.inorder(root, res)
            low, high = 0, len(res)-1
            mid = (low+high)//2
            root = res[mid]
            self.construct(res, root, low, mid-1, True)
            self.construct(res, root, mid+1, high, False)
        return root
