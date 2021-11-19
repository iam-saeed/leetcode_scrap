# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def make_list(elements):
        head = ListNode(elements[0])
        for element in elements[1:]:
            ptr = head
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(elements[element])
        return head

    def print_list(head):
        ptr = head
        print('[', end = " ")
        while ptr:
            print(ptr.val, end = ", ")
            ptr = ptr.next
        print(']')

class Solution:
    def mergeTwoSortedLists(self, l1, l2):
        # if nothing is in the l1 then return l2 else if nothing in l2 then return l1
        if not l1:
            return l2
        if not l2:
            return l1
        
        # if the value in l1 is <= l2 then merge (l1.next, l2) 
        if (l1.val <= l2.val):
            l1.next = self.mergeTwoSortedLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists(l1, l2.next)
            return l2