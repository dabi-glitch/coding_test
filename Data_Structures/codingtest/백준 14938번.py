INF = int(1e9)

n,m,r = map(int,input().split()) #n지역개수 m수색범위 r길

items = list(map(int, input().split())) #길이 가지고 있는 아이템의 개수

maps = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1): 
  for j in range(n+1):
    if i == j:
      maps[i][j] = 0

for i in range(r):
  a,b,c = map(int, input().split()) #a,b, 양 끝 지역 c 가중치
  maps[a][b] = c
  maps[b][a] = c

for k in range(n+1): #플로이드 워셜 알고리즘
  for i in range(n+1):
    for j in range(n+1):
      maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

max_score = 0

for i in range(1,n+1): #각 정점에서 출발해서 얻을 수 있는 아이템 계산
  score = 0
  for j in range(1,n+1):
    if maps[i][j] <= m:
      score += items[j-1] #maps의 인덱스는 1부터, itmes는 0부터 시작이라 -1 해줌
  max_score = max(score, max_score) #최대 아이템 개수 출력

print(max_score)