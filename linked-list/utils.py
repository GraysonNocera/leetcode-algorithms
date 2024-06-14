from list import Node

def array_to_linked_list(array: list) -> Node:
  if len(array) == 0:
    return None
  
  head = Node(array[0], None)
  curr = head
  for value in array[1:]:
    curr.next = Node(value, None)
    curr = curr.next

  return head

def print_linked_list(head: Node) -> None:
  if not head:
    print("Empty list")
    return

  curr = head
  while curr and curr.next:
    print(f"{curr.val} -> ", end="")
    curr = curr.next

  print(f"{curr.val}")

def run_test(array: list, test: callable, args: tuple = (), should_return = True):
  print()
  head = array_to_linked_list(array)
  print_linked_list(head)
  if should_return:
    head = test(head, *args)
  else:
    test(head)
  print_linked_list(head)
  print()