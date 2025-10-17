from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        
        curr = prev.next
        next_node = None

        for _ in range(right-left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next
    
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end="->" if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])
    print("Original List")
    print_linked_list(head)
    sol = Solution()
    new_head = sol.reverseBetween(head,2,4)

    print("AFter List:")
    print_linked_list(new_head)