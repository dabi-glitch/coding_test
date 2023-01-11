arr = []
arr1 = []

for i in range(7):
  arr.append(int(input()))
  if arr[i] % 2 != 0:
    arr1.append(arr[i])

if sum(arr1) == 0:
  print(-1)
else :
  print(sum(arr1))
  print(min(arr1))