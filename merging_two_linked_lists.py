# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,l1,l2):

        dummy=current=ListNode()
        while l1 and l2:


            if l1.val>l2.val:


                current.next=l2
                l2=l2.next
            else:

                current.next=l1
                l1=l1.next
#now let us assume if the list is not empty till now then
            if not l1:

                current.next=l2
            else:

                current.next=l1
            return current.next #the merged list starts from the next of the current node.




