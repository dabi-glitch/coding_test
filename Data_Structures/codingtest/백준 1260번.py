from collections import deque

n, m, v = map(int, input().split())

visit_dfs = [0] * (n+1)
visit_bfs = [0] * (n+1)

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

def dfs(v):
  visit_dfs[v] = 1
  print(v, end=' ')
  
  for i in range(n+1):
    if visit_dfs[i] == 0 and matrix[v][i] == 1:
      dfs(i)


def bfs(v):
  visit_bfs[v] = 1
  queue = deque()
  queue.append(v)

  while queue:
    popV = queue.popleft()
    print(popV, end=' ')
    for i in range(1, n+1):
      if visit_bfs[i] == 0 and matrix[popV][i] == 1:
        queue.append(i)
        visit_bfs[i] = 1

dfs(v)
print()
bfs(v)