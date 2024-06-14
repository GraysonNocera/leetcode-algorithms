"""
Remove one element
"""

from list import Node
from utils import run_test

def remove1(head: Node, target: int):
  curr = head
  prev = None

  if head and target == head.val:
    return head.next

  while curr:
    if curr.val == target:
      prev.next = curr.next
      break      

    prev = curr
    curr = curr.next

  return head

if __name__ == "__main__":
  tests = [
    ([1, 2, 3, 4, 5, 6], 2),
    ([1, 2, 3, 4, 5, 6, 7], 7),
    ([1, 2, 3, 4, 5, 6, 7], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8], 9),
    ([], 1),
    ([1], 1),
    ([1, 2], 1),
  ]

  for args in tests:
    run_test(args[0], remove1, args=(args[1],))