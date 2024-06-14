from utils import run_test, array_to_linked_list
from list import Node

def merge1(head1: Node, head2: Node):
  curr1 = head1
  curr2 = head2
  mergedHead = mergedCurr = Node()

  while curr1 and curr2:
      if curr1.val < curr2.val:
          mergedCurr.next = curr1
          curr1 = curr1.next
      else:
          mergedCurr.next = curr2
          curr2 = curr2.next
      mergedCurr = mergedCurr.next
  
  mergedCurr.next = curr1 or curr2

  return mergedHead.next

if __name__ == "__main__":
  tests = [
    ([1, 2, 3], [4, 5, 6]),
    ([1, 3, 5], [2, 4, 6]),
    ([2, 4, 6], [1, 3, 5]),
    ([], [1, 2]),
    ([1, 2], []),
    ([], []),
    ([1], [1]),
  ]

  for args in tests:
      run_test(args[0], merge1, args=(array_to_linked_list(args[1]),))