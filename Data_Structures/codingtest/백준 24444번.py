from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]

visit = [0] * (n+1)

cnt = 1

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(graph, visit, v):
  global cnt
  queue = deque()
  queue.append(v)
  visit[v] = cnt

  while queue:
    popv = queue.popleft()
    graph[popv].sort()
    for i in graph[popv]:
      if visit[i] == 0:
        queue.append(i)
        cnt+=1
        visit[i] = cnt


bfs(graph, visit, r)

for i in range(1,len(visit)):
  print(visit[i])