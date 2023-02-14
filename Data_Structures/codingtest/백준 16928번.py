from collections import deque

def bfs():
  
  queue = deque()
  queue.append(1)

  visit[1] = 1
  
  while queue:

    now = queue.popleft()

    if matrix[now-1] == 100:
        return visit[100]

    for dice in range(1,7):
      next_visit = now + dice

      if next_visit > 100:
        continue

      if next_visit in moves:
        next_visit = moves[next_visit]

      if visit[next_visit] == 0:
        visit[next_visit] = 1 + visit[now]
        queue.append(next_visit)

ladder, snake = map(int, input().split())

moves = {}

for i in range(ladder+snake):
  a,b = map(int, input().split())
  moves[a] = b

matrix = [i for i in range(1,101)] #게임판

visit = [0] * 101

print(bfs()-1)