from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().rstrip().split()) #n은 행, m은 열
maps = [list(map(int, input().rstrip())) for _ in range(n)]
walls = [] 
answer = [] #n,m에 도달하기 위해 걸린 값들

for i in range(n):
  for j in range(m):
    if maps[i][j] == 1:
      walls.append((i,j))

def bfs():
  queue = deque()
  queue.append((0,0))
  maps[0][0] = 2

  while queue:
    x,y = queue.popleft()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      
      if maps[nx][ny] == 1:
        continue

      if maps[nx][ny] == 0:
        maps[nx][ny] = maps[x][y]+1
        queue.append((nx,ny))
        maps[nx][ny] = 0

  print(maps)
  return maps[n-1][m-1]

x = bfs()
maps[0][0] = 0
if x != 0:
   answer.append(x)

for i in walls:
    maps[i[0]][i[1]] = 0
    x = bfs()
    maps[i[0]][i[1]] = 1
    if x != 0:
        answer.append(x)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer)-1)