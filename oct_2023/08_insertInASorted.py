# iven a linked list sorted in ascending order and an integer called data,
# insert data in the linked list such that the list remains sorted

class Solution:
    def sortedInsert(self,head,key):
        new_node = Node(key)
        
        if head is None or head.data>=key:
            # if new node is needed at the start of list
            new_node.next = head
            return new_node
        
        current = head
        
        while (current.next is not None) and current.next.data<key:
            current = current.next;
            # finding a node which has lesser value than new_node
            # but its successor should have greater (or equal) value
        
        # inserting new_node after current node
        new_node.next = current.next;
        current.next = new_node;
        
        return head
