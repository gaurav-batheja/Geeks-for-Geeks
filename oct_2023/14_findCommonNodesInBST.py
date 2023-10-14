# Given two Binary Search Trees. Find the nodes that are common in both of them, ie- find the intersection of the two BSTs.

# Note: Return the common nodes in sorted order.


class Solution:
    def findCommon(self, root1, root2):
        def inOrderTraversal(root, result):
            if not root:
                return
            inOrderTraversal(root.left, result)
            result.append(root.data)
            inOrderTraversal(root.right, result)
        
        result1, result2 = [], []
        inOrderTraversal(root1, result1)
        inOrderTraversal(root2, result2)

        common_elements = []
        i, j = 0, 0

        while i < len(result1) and j < len(result2):
            if result1[i] == result2[j]:
                common_elements.append(result1[i])
                i += 1
                j += 1
            elif result1[i] < result2[j]:
                i += 1
            else:
                j += 1

        return common_elements
