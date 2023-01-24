import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
num = sorted(set(arr))

dic = {num[i]:i for i in range(len(num))}
for i in arr:
  print(dic[i], end=' ')
