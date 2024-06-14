from list import Node
from utils import array_to_linked_list, print_linked_list

def reverse1(head):
  curr = head
  prev = None

  while curr:
    temp = curr.next
    curr.next = prev # only actually switching one pointer: (   4 -> ) becomes ( <- 4   )
    prev = curr
    curr = temp

  return prev


if __name__ == "__main__":
  arr = [1, 2, 3, 4]
  head = array_to_linked_list(arr)
  print_linked_list(head)
  reversed_head = reverse1(head)
  print_linked_list(reversed_head)