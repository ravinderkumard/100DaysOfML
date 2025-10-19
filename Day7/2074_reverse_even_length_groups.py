"""
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
Example 2:


Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.
Example 3:


Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 105
"""


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        groupCount = 1
        prev = dummy
        while head:
            count = 1
            end = head
            while end.next and count<groupCount:
                count+=1
                end = end.next
            nextGroupFirst = end.next
            if count%2==0:
                rev = self.rever(head,count)
                prev.next = rev[0]
                rev[1].next = nextGroupFirst
                prev = rev[1]
            else:
                prev = end
            groupCount+=1
            head = nextGroupFirst
        return dummy.next
    def rever(self,head,count):
        curr = head
        prev = None
        while curr and count>0:
            count-=1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return [prev,head]