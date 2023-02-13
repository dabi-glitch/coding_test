from collections import deque
import sys

input = sys.stdin.readline

m,n,h = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(n)]for _ in range(h)] #첫 상태

queue = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if matrix[i][j][k] == 1:
        queue.append((i,j,k)) #z,y,x순서서

def bfs():
  while queue:
  
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    z,y,x = queue.popleft()
  

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if nx<0 or ny<0 or nz<0 or nx>=m or ny>=n or nz>=h:
        continue
    
      if matrix[nz][ny][nx] == -1:
        continue

      if matrix[nz][ny][nx] == 0:
        matrix[nz][ny][nx] = matrix[z][y][x] + 1
        queue.append((nz,ny,nx))

bfs()

check = 0
result = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if matrix[i][j][k] == 0:
        check +=1
        break
      else:
        result = max(result, max(matrix[i][j]))
        
if check != 0:
  print(-1)
else:
  print(result-1)

