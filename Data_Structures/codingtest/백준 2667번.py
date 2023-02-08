from collections import deque

n = int(input())

total = [list(map(int, input())) for i in range(n)]
result = [] #단지 개수를 담을 LIST
dx = [-1,1,0,0] #좌우 이동을 위한 좌표
dy = [0,0,-1,1] #상하 이동을 위한 좌표

def bfs(total, x,y):

    queue = deque()
    queue.append((x,y))
    total[x][y] = 0 #한 번 다녀온 곳은 재방문을 방지하기 위해 0으로 바꿈
    cnt = 1 #단지에 속해있는 아파트 개수

    while queue:
      x,y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny <0 or nx >= n or ny >=n: #정사각형의 범위에서 넘어가면 멈춤
          continue 
        if total[nx][ny] == 0: #벽을 만나면 멈춤
          continue
        if total[nx][ny] == 1:
          total[nx][ny] = 0
          queue.append((nx,ny)) 
          cnt+=1
    return cnt


for i in range(n):
  for j in range(n): 
    if total[i][j] == 1: 
      cnt = bfs(total, i, j)
      result.append(cnt)

result.sort() #오름차순 정렬

print(len(result))
for k in result:
  print(k)