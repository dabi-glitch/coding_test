import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input().rstrip()) #집의 크기

house = [list(map(int, input().rstrip().split())) for _ in range(n)]


def dfs(x,y,state):
  global cnt

  if x == n-1 and y == n-1:
    cnt+=1

  #대각선 이동
  if x+1<n and y+1<n:
    if house[x+1][y] == 0 and house[x+1][y+1] == 0 and house[x][y+1]== 0:
      dfs(x+1,y+1,"z")

  #가로 이동
  if state == "x" or state == "z":
    if y+1<n:
      if house[x][y+1] == 0:
        dfs(x,y+1,"x")
        
  #세로 이동
  if state == "y" or state == "z":
    if x+1<n:
      if house[x+1][y] == 0:
        dfs(x+1,y,"y")

#도착점에 벽이 있을 경우
if house[n-1][n-1] == 1:
  print(0)
else:
  cnt = 0
  dfs(0,1,"x")
  print(cnt)