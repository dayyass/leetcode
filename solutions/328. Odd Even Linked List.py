# Solution 1
# Time: O(n), Space: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head


# Solution 2
# Time: O(n), Space: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(-1), ListNode(-1)
        odd_head, even_head = odd, even
        is_odd = True
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            is_odd = not is_odd
        even.next = None
        odd.next = even_head.next
        return odd_head.next
