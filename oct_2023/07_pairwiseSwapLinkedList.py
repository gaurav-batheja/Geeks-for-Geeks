# Given a singly linked list of size N. The task is to swap elements in the linked list pairwise.
# For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.
# Note: You need to swap the nodes, not only the data. If only data is swapped then driver will print -1

class Solution:    
    def pairWiseSwap(self, head):
        # code here
        temp = head
        while temp and temp.next:
            if temp.data != temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
        temp = head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
