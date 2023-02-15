n = int(input())

def stack():
  stack = []

  for i in arr:
    if i == "(" :
      stack.append("(")
      continue

    if i == ")":
        if stack:
            stack.pop()
        else:
            print("NO")
            break

  if len(stack) > 0:
    return "NO"
  else:
    return "YES"

for i in range(n):
  arr = list(input())
  print(stack())
   