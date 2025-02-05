class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    The key points to understand are:
    The digits are stored in reverse order (342 is stored as 2->4->3)
    Each node contains a single digit
    We need to handle carry-over when adding digits
    We need to handle lists of different lengths
    The result should also be in reverse order
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2:
            
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            
            carry, curr.next = divmod(total, 10)
            curr.next = ListNode(curr.next)
            curr = curr.next
        
        
        if carry:
            curr.next = ListNode(carry)
            
        return dummy.next
        