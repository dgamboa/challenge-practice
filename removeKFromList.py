# Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

# Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

# Example

# For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
# removeKFromList(l, k) = [1, 2, 4, 5];
# For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
# removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].

# Initial Submission:
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    if l is None:
        return l
    
    cur = l
    while cur is not None:
        if cur.value == k:
            l = l.next
            cur = l
        elif cur.next is not None and cur.next.value == k:
            temp = cur.next
            cur.next = temp.next
            temp.next = None
        else:
            cur = cur.next
    
    return l


# Top Submission:
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l
