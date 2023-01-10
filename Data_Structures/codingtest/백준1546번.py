N = int(input())
A = list(map(int,input().split()))
B = []
best = max(A)
result = 0

for i in range(len(A)):
  result = (A[i]/best)*100
  B.append(result)

result = 0

for i in range(len(A)):
  result = B[i]+result
  avg = result/N

print(avg)