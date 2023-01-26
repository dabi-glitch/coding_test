#숫자카드게임

n, m = map(int, input().split()) #n=행,m=열

arr1 = []
for i in range(n):
  arr = list(map(int,input().split()))
  arr1.append(min(arr))

print(max(arr1))
