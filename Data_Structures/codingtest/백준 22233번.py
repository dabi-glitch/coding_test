import sys

input = sys.stdin.readline

n,m = map(int, input().split())

keyword = {}

for i in range(n):
  keyword[input().rstrip()] = 1

for i in range(m):
  rmv = input().rstrip().split(",")  
  for i in rmv:
    if i in keyword:
      keyword.pop(i)
  print(len(keyword.keys()))