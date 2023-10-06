# Given a linked list, you have to perform the following task:
# Extract the alternative nodes starting from second node.
# Reverse the extracted list.
# Append the extracted list at the end of the original list.

class Solution:
    def rearrange(self, head):
        # If the list has less than 3 nodes, no rearrangement is needed
        if head is None or head.next is None or head.next.next is None:
            return head

        # Initialize two pointers for the even and odd nodes
        even = head
        odd = head.next

        # Save the head of the odd list to attach at the end
        odd_head = odd

        # Traverse the list to separate the even and odd nodes
        while even.next is not None and odd.next is not None:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next

        # If there are an even number of nodes, the last even node will be None
        if even.next is not None:
            even.next = None

        # Reverse the odd list
        prev_node = None
        curr_node = odd_head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        # Attach the reversed odd list at the end of the even list
        even.next = prev_node

        return head
