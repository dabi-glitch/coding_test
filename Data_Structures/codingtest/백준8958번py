n = int(input())

for _ in range(n):
  arr = list(input()) 
  b = []
  sum = 0
  for i in range(len(arr)):
    if i == 0:
      if arr[i] == 'O':
        b.append(1)
        sum = sum+1
      else :
        b.append(0)
    else :
      if arr[i] == 'O':
        b.append(b[i-1]+1)
        sum = sum + b[i]
      else:
        b.append(0)
  print(sum)