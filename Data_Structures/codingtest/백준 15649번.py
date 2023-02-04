from itertools import permutations

n, m = map(int, input().split())

arr = []

for i in range(1,n+1):
  arr.append(i)

for j in permutations(arr, m):
  for i in j:
    print(i, end=' ')
  print()
