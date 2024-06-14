from list import Node
from utils import run_test

def midpoint1(head: Node) -> Node:
  """
  Slow is the midpoint of the list.
  For even size: slow contains the (len/2)th element, fast is None
  For odd size: slow contains the (len//2)th element, fast is the last element
  """

  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

if __name__ == "__main__":
  tests = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7],
    [],
    [1],
    [1, 2],
  ]

  for array in tests:
    run_test(array, midpoint1, should_return=True)