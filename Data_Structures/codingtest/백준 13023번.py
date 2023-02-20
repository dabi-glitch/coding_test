import sys
sys.setrecursionlimit(10**9)

def dfs(v,cnt):
  
  if cnt == 4:
    print(1)
    exit()
  for i in relation[v]:
    if visit[i] == 0:
      visit[i] = 1
      dfs(i, cnt+1)
      visit[i] = 0
    

n,m = map(int, input().rstrip().split()) #n=친구수 m=관계수

relation = [[] for _ in range(n)]

visit = [0] * n

for i in range(m):
  a,b = map(int, input().rstrip().split())
  relation[a].append(b)
  relation[b].append(a)

for i in range(n):
  visit[i] = 1
  dfs(i,0)
  visit[i] = 0
        
print(0)