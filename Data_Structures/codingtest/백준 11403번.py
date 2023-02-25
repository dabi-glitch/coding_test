n = int(input()) #정점

graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

for k in range(n): #경유지
 for i in range(n): #출발
   for j in range(n): #도착
     if graph[i][k] and graph[k][j]:
       graph[i][j] = 1
     
for i in range(n):
  for j in range(n):
    print(graph[i][j], end=" ")
  print()