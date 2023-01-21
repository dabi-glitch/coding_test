n,m = map(int, input().split())
num = list(map(int, input().split()))
result = []

for i in range(n):
  arr = []
  arr.append(num[i])
  for j in range(i+1,n):
    arr.append(num[j])
    arr = [num[1]]
    for h in range(j+1,n):
      arr = [num[i],num[j]]
      arr.append(num[h])
      if sum(arr) <= m:
        result.append(sum(arr))

print(max(result))