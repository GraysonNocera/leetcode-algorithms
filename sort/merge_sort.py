import copy

def merge1(array: list) -> list:
  recursive_merge_sort(array, 0, len(array) - 1)

def recursive_merge_sort(array: list, l: int, r: int):
  if l >= r:
    return
  
  m = (l + r) // 2
  recursive_merge_sort(array, l, m)
  recursive_merge_sort(array, m + 1, r)
  merge_subarrays(array, l, m, r)

def merge_subarrays(array: list, l: int, m: int, r: int):
  L = array[l:(m + 1)]
  R = array[(m + 1):(r + 1)]

  i = j = 0
  k = l
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      array[k] = L[i]
      i += 1
    else:
      array[k] = R[j]
      j += 1
    k += 1
  
  while i < len(L):
    array[k] = L[i]
    i += 1
    k += 1
  while j < len(R):
    array[k] = R[j]
    j += 1
    k += 1

if __name__ == "__main__":
  tests = [
    [3, 6, -1, 4, 2, 1, 9, 4, 8],
    [],
    [1, -1],
    [-1],
    [3, 2, 4],
  ]

  for test in tests:
    test_copy = copy.deepcopy(test)
    merge1(test)
    test_copy.sort()
    assert test == test_copy
    print(test)