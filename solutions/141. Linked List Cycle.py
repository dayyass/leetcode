# Solution 1 (optimal): Floyd's Cycle Finding Algorithm, Two Pointers
# Time: O(n), Space: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Solution 2: Hash Table
# Time: O(n), Space: O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
