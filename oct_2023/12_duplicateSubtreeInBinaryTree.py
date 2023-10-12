# Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.

# Note: Two same leaf nodes are not considered as subtree as size of a leaf node is one.
# Node Class:
"""
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def sub_tree_value(self,root,sub_tree):
        if root is None:
            return '#'
        
        sub_string = str(root.data) + self.sub_tree_value(root.left,sub_tree) + self.sub_tree_value(root.right,sub_tree)
        if sub_string in sub_tree:
            sub_tree[sub_string] += 1
        else:
            sub_tree[sub_string] = 1
        return sub_string
        
    def dupSub(self, root):
        sub_tree = {}
        self.sub_tree_value(root,sub_tree)
        for key,valie in sub_tree.items():
            if len(key) > 3 and valie >=2:
                return 1
        return 0
