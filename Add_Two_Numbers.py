class Solution:
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
        