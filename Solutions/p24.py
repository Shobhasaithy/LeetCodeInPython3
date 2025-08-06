# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge cases (e.g., swapping the head node)
        dummy = ListNode(0, head)
        prev = dummy 
        cur = head
        
        # Traverse the list in pairs
        while cur and cur.next:
            # Store the node after the next to reconnect later
            temp = cur.next.next
            
            # Identify the two nodes to swap
            first = cur 
            second = cur.next
            
            # Swap the nodes
            second.next = first
            first.next = temp 
            
            # Connect the previous part to the new front of this pair
            prev.next = second
            
            # Move pointers forward for the next pair
            prev = first
            cur = temp 

        # Return the new head of the list
        return dummy.next



'''
Better to draw it to visulaize connections, works the best.
'''
