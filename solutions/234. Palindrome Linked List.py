# Solution 1 (optimal): But change input linked list
# Time: O(n), Space: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # get middle (slow)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse right (prev)
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True


# TODO:
# Restore the list
