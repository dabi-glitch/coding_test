from collections import deque

n,m = map(int, input().split()) #n=행 m=열


matrix = [list(map(int,input().split())) for _ in range(n)] #주어진 map

arr = [] #아기 상어들의 위치

answer = []

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
      arr.append((i,j))

def bfs(i):

    queue = deque()
    queue.append(arr[i])
    result = []
    visit[arr[i][0]][arr[i][1]] = 1

    dx = [1,1,1,0,-1,-1,-1,0]
    dy = [-1,0,1,1,1,0,-1,-1]

    while queue:
    
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            if visit[nx][ny] == 1:
                continue

            if visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx,ny))
                if matrix[nx][ny] == 1:
                    result.append(visit[nx][ny]-2)

    return result


for i in range(len(arr)):
    visit = [[0] * m for _ in range(n)]
    answer.append(bfs(i))
    print(answer)
    print(matrix)

