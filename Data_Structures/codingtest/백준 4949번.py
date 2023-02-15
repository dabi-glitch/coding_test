
arr = list(input())

stack = []
  
for i in arr:
    if len(stack) == 0:
        stack.append(i)

    if i == "(" or i == "[":
      stack.append(i)
    
    if i == ")" and stack[-1] == "(":
      stack.pop()
    
    if i == "]" and stack[-1] == "[":
      stack.pop()

  
if len(stack) > 0:
    print("no")
else:
    print("yes")