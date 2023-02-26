from collections import deque

n = int(input()) #배열의 길이

maps = [list(map(int, input().split())) for _ in range(n)]

def bfs(start):

  visit[start[0]][start[1]] = 1
  queue = []
  queue = deque()
  queue.append(start)

  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  while queue:

    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
    
      if maps[nx][ny] != -1 and visit[nx][ny] == 0: #맵이 물에 잠기지 않았고 방문한 적 없는 경우
        visit[nx][ny] = 1
        queue.append((nx,ny))

rain = 0
max_cnt = 0

while True:
  visit = [[0] * n for _ in range(n)] #매 번 visit는 초기화 시켜줌
  cnt = 0

  for i in range(n): #rain보다 높이가 낮으면 visit, maps 모두 -1
    for j in range(n):
      if maps[i][j] <= rain:
        maps[i][j] = -1
        visit[i][j] = -1

  for i in range(n): #전체 maps을 돌며 떨어져있는 안전영역을 찾음
    for j in range(n):
      if maps[i][j] != -1 and visit[i][j] == 0:
        bfs((i,j))
        cnt += 1 # 안전영역의 개수만큼 cnt를 증가시킴
  
  rain += 1

  if cnt == 0: #모두 물에 잠길경우 break
    break
  else:
    max_cnt = max(max_cnt, cnt)

print(max_cnt)