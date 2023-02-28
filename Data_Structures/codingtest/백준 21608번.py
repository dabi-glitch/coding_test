n = int(input())
num = n**2

empty_seat = [(i,j) for i in range(n) for j in range(n)]
result_seat = [[0] * n for _ in range(n)]
loves_seat = [[0] * n for _ in range(n)]

def search(x,y): #빈자리와 좋아하는 학생 수 찾기
  cnt1 = 0
  cnt2 = 0
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny<0 or nx>=n or ny>=n:
      continue
    
    if result_seat[nx][ny] in (b,c,d,e):
      cnt1-=1
    
    elif result_seat[nx][ny] == 0:
      cnt2-=1

  return cnt1,cnt2,x,y

for i in range(num): #최종 자리 만들기
  cnt = []
  a,b,c,d,e = map(int, input().split())

  for k in empty_seat:
    cnt.append(search(k[0],k[1]))
    cnt = sorted(cnt, key = lambda x :(x[0],x[1],x[2],x[3]))    
  result_seat[cnt[0][2]][cnt[0][3]] = a
  loves_seat[cnt[0][2]][cnt[0][3]] = [b,c,d,e]
  empty_seat.remove((cnt[0][2],cnt[0][3]))

answer = 0

visit = [0 for _ in range(num+1)]

def happy(x,y):
  
  visit[result_seat[x][y]] = 1

  global answer  
  
  cnt3 = 0
  
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny<0 or nx>=n or ny>=n:
      continue

    if visit[result_seat[nx][ny]] == 0:
      happy(nx,ny)

    if result_seat[nx][ny] in loves_seat[x][y]:
      visit[result_seat[x][y]] += 1

  if visit[result_seat[x][y]] == 2:
    answer +=1
  
  elif visit[result_seat[x][y]] == 3:
    answer +=10

  elif visit[result_seat[x][y]] == 4:
    answer +=100
  
  elif visit[result_seat[x][y]] == 5:
    answer +=1000

happy(1,1)

print(answer)

      