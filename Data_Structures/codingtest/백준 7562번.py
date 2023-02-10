from collections import deque

t = int(input()) #테스트 케이스 횟수

def bfs():

  #이동할 수 있는 좌표
  dx = [2,2,1,1,-2,-2,-1,-1]
  dy = [-1,1,-2,2,-1,1,-2,2]

  queue = deque()
  queue.append((start_x,start_y))
  maps[start_x][start_y]= 1

  while queue:
    x,y = queue.popleft()
    if x == end_x and y == end_y:
      print(maps[x][y]-1)
      return
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue

      if maps[nx][ny] == 0:
        maps[nx][ny] = maps[x][y] + 1
        queue.append((nx,ny))

for _ in range(t):
  n = int(input()) #체스판 한 변의 길이
  maps = [[0]*n for _ in range(n)]
  start_x,start_y = map(int,input().split())
  end_x,end_y = map(int, input().split())
  bfs()