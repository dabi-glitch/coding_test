import sys

input = sys.stdin.readline

n = int(input().rstrip()) #도시
m = int(input().rstrip()) #버스

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

for i in range(m):
  a,b,c = map(int, input().rstrip().split()) #a시작,b도착,c비용
  graph[a][b] = min(graph[a][b],c)

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print(0, end = " ")
    else:
      print(graph[a][b], end = " ")
  print()