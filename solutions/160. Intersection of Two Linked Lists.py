# Solution 1 (optimal): Two Pointers
# Time: O(n), Space: O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        while currA != currB:
            if currA:
                currA = currA.next
            else:
                currA = headB
            if currB:
                currB = currB.next
            else:
                currB = headA
        return currA


# Solution 2: Hash Table
# Time: O(n), Space: O(n)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        
        # traverse headA
        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next
        
        # traverse headB
        curr = headB
        while curr:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next

        return None
