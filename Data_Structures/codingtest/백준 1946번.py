t = int(input())

for i in range(t):
  n = int(input()) #지원자 수
  apply = []
  top = 0
  cnt = 1
  for i in range(n):
    apply.append(list(map(int,input().split())))
  
  apply.sort()

  for i in range(1,n):
    if apply[i][1] < apply[top][1]:
      top = i
      cnt+=1

  print(cnt)
