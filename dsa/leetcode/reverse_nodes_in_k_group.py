# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head is None) or (head.next is None) or (k == 0):
            return head

        j = k
        prev = None
        cur = head
        cur_next = cur.next
        while (j > 0) and (cur is not None):
            cur.next = prev
            prev = cur
            cur = cur_next
            if cur_next:
                cur_next = cur_next.next
            j = j - 1

        if j == 0:
            head.next = self.reverseKGroup(cur, k)
        else:
            cur = prev
            prev = None
            cur_next = cur.next
            while prev != head:
                cur.next = prev
                prev = cur
                cur = cur_next
                if cur_next and cur_next.next:
                    cur_next = cur_next.next
            return head
        return prev