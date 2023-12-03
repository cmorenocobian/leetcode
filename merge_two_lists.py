'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cursor = anchor = ListNode()
        # Recorro las listas y voy añadiendo los elementos
        while list1 and list2:
            # Comparo y añado el elemento menor
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
            # muevo al siguiente elemento
            cursor = cursor.next
        
        # Enlace al resto de la lista no vacía
        cursor.next = list1 if list1 else list2
        return anchor.next