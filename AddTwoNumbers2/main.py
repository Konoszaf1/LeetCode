from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        print_string = ""
        next_node = self
        while next_node is not None:
            print_string += f"{next_node.val} "
            next_node = next_node.next
        return print_string

def get_number(node: ListNode) -> int:
    number = f"{node.val}"
    while node.next is not None:
        node = node.next
        number += f"{node.val}"
    return int(number[::-1])

def create_list(number: int) -> ListNode:
    node = ListNode(int(str(number)[-1]))
    return_node = node
    for digit in str(number)[-2::-1]:
        node.next = ListNode(int(digit))
        node = node.next
    return return_node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return create_list(get_number(l1) + get_number(l2))


if __name__ == "__main__":
    l3 = ListNode(3, None)
    l2 = ListNode(4, l3)
    l1 = ListNode(2, l2)

    l6 = ListNode(4, None)
    l5 = ListNode(6, l6)
    l4 = ListNode(5, l5)
    print(Solution().addTwoNumbers(l1, l4))