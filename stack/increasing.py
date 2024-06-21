
def daily_temps(temperatures: list) -> list: 
  res = [0] * len(temperatures)
  stack = []  # pair: [temp, index]

  for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]: # popping while top of the stack is less than the current temperature to keep it monotonically increasing
      _, stackInd = stack.pop()
      res[stackInd] = i - stackInd
    stack.append((t, i))
  return res

if __name__ == "__main__":
   tests = [
      [30,38,30,36,35,40,28],
      [22,21,20],
   ]

   for test in tests:
      print(daily_temps(test))