from collections import deque

n = int(input()) #정점
m = int(input()) #간선

matrix = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

visit = [0] * (n+1)

def bfs(v):
  visit[v] = 1
  queue = deque()
  queue.append(v)
  
  while queue:
    popV = queue.popleft()
    for i in range(1,n+1):
      if visit[i] == 0 and matrix[popV][i] == 1:
        visit[i] = 1
        queue.append(i)

bfs(1)

print((visit.count(1)) - 1)