from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(self.to_array())

    def to_array(self):
        result = []
        x = self
        while x:
            result.append(x.val)
            x = x.next
        return result


def array_to_listnodes(arr: List[int]) -> ListNode:
    """
    Converts array of integers into linked list of {ListNode} and returns first element
    """
    if len(arr) <= 0:
        raise ValueError(f'invalid input ={arr}')

    first = ListNode(arr[0])
    if len(arr) == 1:
        return first

    last = ListNode(arr[1])
    first.next = last

    for i in range(2, len(arr)):
        next = ListNode(arr[i])
        last.next = next
        last = next

    return first


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tn = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)),
                 TreeNode(3,
                          TreeNode(6),
                          TreeNode(7)))
