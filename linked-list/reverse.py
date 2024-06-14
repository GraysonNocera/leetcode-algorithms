from list import Node
from utils import run_test

def reverse1(head: Node):
  curr = head
  prev = None

  while curr:
    temp = curr.next
    curr.next = prev # only actually switching one pointer: (   4 -> ) becomes ( <- 4   )
    prev = curr
    curr = temp

  return prev


if __name__ == "__main__":
  tests = [
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5, 6, 7],
    [],
    [1],
    [1, 2]
  ]
  for arr in tests:
    run_test(arr, reverse1, should_return=True)