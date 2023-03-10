import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):

  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().rstrip().split()) #n=집합의 개수 m=연산의 개수

parent = [0] * (n+1) #이 문제는 0부터 시작함

for i in range(n+1):
  parent[i] = i

for _ in range(m):
  op,a,b = map(int,input().rstrip().split())
  if op == 0:
    union_parent(parent,a,b)
  else:
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a != b:
      print("NO")
    else:
      print("YES")
