# Solution 1 (optimal): Two Pointers
# Time: O(n), Space: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


# Solution 2: Straightforward
# Time: O(n), Space: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        # remove
        idx = length - n
        if idx == 0:
            head = head.next
        else:
            curr = head
            for _ in range(idx - 1):
                curr = curr.next
            curr.next = curr.next.next
        return head
