import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))

result = sorted(arr, key = lambda x:(x[1],x[0]))

for i in result:
  print(i[0],i[1])