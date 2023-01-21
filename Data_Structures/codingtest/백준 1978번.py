n = int(input())
cnt = 0
num = list(map(int, input().split()))
rmv_list=[]

arr = list(range(1,1001))

for i in range(2,1001):
  for j in range(2,1001):
    if i*j <= 1000:
      rmv_list.append(i*j)
result = set(arr) - set(rmv_list)

for n in num:
  if n in result:
    if n == 1:
      pass
    else:
      cnt += 1

print(cnt)