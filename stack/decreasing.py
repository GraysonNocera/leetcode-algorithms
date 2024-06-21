import increasing

def daily_temps(temperatures: list) -> list: 
  stack = []
  output = [0] * len(temperatures)

  for i in range(len(temperatures) - 1, -1, -1):
    while stack and temperatures[stack[-1]] <= temperatures[i]:
      stack.pop()
    if stack: output[i] = stack[-1] - i
    else: output[i] = 0
    stack.append(i)
  return output

if __name__ == "__main__":
   tests = [
      [30,38,30,36,35,40,28],
      [22,21,20],
   ]

   for test in tests:
      print(daily_temps(test))
      assert increasing.daily_temps(test) == daily_temps(test)