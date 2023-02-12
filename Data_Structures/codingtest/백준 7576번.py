from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(m):
  arr.append(list(map(int, input().split())))

arr2 = [] #처음 시작이 1인 좌표
cnt = 0

for i in range(m):
  for j in range(n):
    if arr[i][j] == 1:
      arr2.append((i,j))

def bfs():
  global cnt
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  
  arr1 = deque()
  queue = deque()

  for i in arr2:
    arr1.append(i)
    queue.append(i)

  while queue:
    while arr1:
      x,y = arr1.popleft()
      queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n:
          continue
        if arr[nx][ny] == -1:
          continue
        if arr[nx][ny] == 0:
          arr[nx][ny] = 1
          queue.append((nx,ny))
    for i in queue:
      arr1.append(i)
    cnt+=1
  return True

bfs()

check = 0
for i in range(m):
  if 0 in arr[i]:
    check +=1
    break

if check == 0:
  print(cnt-1)
else: print(-1)
