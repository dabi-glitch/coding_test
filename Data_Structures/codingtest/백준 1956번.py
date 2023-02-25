INF = int(1e9)

v,e = map(int, input().split()) #v마을 e도로

dist = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
  a,b,c = map(int, input().split())
  dist[a][b] = c

for k in range(1,v+1):
  for i in range(1,v+1):
    for j in range(1,v+1):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

result = INF

for i in range(1,v+1):
  result = min(result, dist[i][i])

if result != INF:
  print(result)
else:
  print(-1)