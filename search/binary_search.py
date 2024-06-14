
def binary_search1(array: list, target: int):

  l, r = 0, len(array) - 1
  while l <= r:
    m = (l + r) // 2
    if array[m] == target:
      return m
    elif array[m] > target:
      r = m - 1
    else:
      l = m + 1

  return -1



if __name__ == "__main__":
  tests = [
    ([1, 2, 3, 4, 5, 6], 5),
    ([1, 2, 3, 4, 5, 6], 1),
    ([1, 2, 3, 4, 5, 6], 6),
    ([1], 0),
    ([1], 1),
    ([2, 3, 3, 4, 5, 6, 8, 8, 8, 8], 7)
  ]

  for args in tests:
    index = binary_search1(args[0], args[1])
    print(f"Searched {args[0]} for {args[1]} and found it at index {index}: {args[0][index] if index >= 0 else -1}")
