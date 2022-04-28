# Time: O(n), Space: O(n)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0            
            summ = x + y + carry
            carry = summ // 10
            z = summ % 10
            curr.next = ListNode(z)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
