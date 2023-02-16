t = int(input())

for i in range(t):

  n = int(input())

  d = [0,1,2,4] #1,2,3을 만들 수 있는 경우의 수

  if n > 3:

    d = d + [0] * (n-3)

    for i in range(4,n+1):
      d[i] = d[i-1] + d[i-2] + d[i-3]

  print(d[n])