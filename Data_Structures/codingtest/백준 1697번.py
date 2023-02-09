from collections import deque

n, k = map(int, input().split())

max_num = 100000

visit = [0] * (max_num+1)

def bfs():
  queue = deque() 
  queue.append(n)

  while queue:
    x = queue.popleft()

    if x == k:
      print(visit[x])
      break
    
    for j in (x-1, x+1, x*2):
      if 0<=j<= max_num and visit[j] == 0:
        visit[j] = visit[x] + 1
        queue.append(j)

bfs()
