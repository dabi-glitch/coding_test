import sys

n = int(sys.stdin.readline())
s_number = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
total_number = list(map(int, sys.stdin.readline().split()))
arr = []

for i in total_number:
  start = 0 
  end = n-1

  while start <= end:
    mid = (start+end)//2  
    result = 0
    if s_number[mid] == i:
      result = 1
      break
    elif s_number[mid] > i:
      end = mid-1
    elif s_number[mid] < i:
      start = mid+1

  if result == 1:
    arr.append(1)
  else:
    arr.append(0)

for i in arr:
  print(i, end=' ')