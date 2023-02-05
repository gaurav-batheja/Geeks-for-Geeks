#Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.
#The task is to complete the function intersetPoint() which takes the pointer to the head of linklist1(head1) and linklist2(head2) as input parameters and returns data value of a node where two linked lists intersect. If linked list do not merge at any point, then it should return -1.
#Challenge : Try to solve the problem without using any extra space.
    def intersetPoint(self,head1,head2):
        ah,bh=head1,head2
        while(ah!=bh):
         ah=ah.next if ah else head2
         bh=bh.next if bh else head1
        return ah.data
 
