# Solution 1 (optimal): Dummy Head
# Time: O(n), Space: O(1)

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy head
        dummy_head = ListNode(-1, next=head)
        
        curr = dummy_head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_head.next


# TODO:
# Recursive solution
