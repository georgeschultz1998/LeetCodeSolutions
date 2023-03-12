# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1, val2 = [],[]  # initialize empty lists to store the string representation of values of linked lists
        while l1:
            val1.append(str(l1.val))  # add the string representation of the value to the list
            l1 = l1.next  # move to the next node
        while l2:
            val2.append(str(l2.val))  # add the string representation of the value to the list
            l2 = l2.next  # move to the next node

        val1.reverse()  # reverse the lists to add the values from the rightmost digit
        val2.reverse()
        val1 = "".join(val1)  # join the string representation of values to form a single number
        val2 = "".join(val2)
        finalVal = int(val1) + int(val2)  # add the two numbers
        finalVal = str(finalVal)[::-1]  # convert the number to string and reverse it

        l3 = ListNode(finalVal[0])  # create the first node of the resulting linked list with the first digit
        cur = l3  # initialize a current pointer to point to the last node of the linked list
        for num in str(finalVal)[1:]:  # iterate over the remaining digits of the number
            cur.next = ListNode(int(num))  # create a new node with the digit and add it to the linked list
            cur = cur.next  # move the current pointer to the last node

        return l3  # return the head of the resulting linked list
