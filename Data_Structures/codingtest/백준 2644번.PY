from collections import deque

def bfs():
  queue = deque()
  queue.append(a)
  visit[a] = 0

  while queue:
    x = queue.popleft()
    if x == b:
      return visit[x]
    else:
      for i in graph[x]:
        if visit[i] == 0:
          visit[i] = visit[x]+1
          queue.append(i)

total = int(input()) #전체 사람 수
a,b = map(int, input().split())
family = int(input()) #부모 가족 수
graph = [[] for i in range(total + 1)]
visit = [0] * (total+1)
for i in range(family):
  c,d = map(int, input().split())
  graph[c].append(d)
  graph[d].append(c)

bfs()

if visit[b] == 0:
  print(-1)
else:
  print(visit[b])