INF = int(1e9)

t = int(input()) #테스트케이스

def bf(start):
  
  dist[start] = 0

  for i in range(n+1):
    for j in range(len(edges)):
      cur = edges[j][0]
      next_node = edges[j][1]
      cost = edges[j][2]

      if dist[cur] != INF and dist[next_node] > cost + dist[cur]:
        dist[next_node] = cost + dist[cur]
        if i == (x-1):
          return True
  return False


for _ in range(t):
  
  n,m,w = map(int,input().split()) #n지점 m도로 w웜홀

  x = n+1

  edges = [(x,i,0) for i in range(1,n+1)]

  dist = [INF] * (n+2)

  for _ in range(m): #도로
    s,e,t = map(int,input().split()) #s출발 e도착 t가중치
    edges.append((s,e,t))
    edges.append((e,s,t))

  for _ in range(w): #웜홀
    s,e,t = map(int,input().split())
    edges.append((s,e,-t))

  cycle = bf(n+1)

  if cycle:
    print("YES")
  else:
    print("NO")