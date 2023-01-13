import sys

N = int(sys.stdin.readline())
arr = [0] * 10001  #0부터 10000까지 이기 때문에 10001개

for _ in range(N):
  num = int(sys.stdin.readline()) 
  arr[num] += 1 #num이 들어온 개수 count

for i in range(10001):
  if arr[i] != 0 :
    for j in range(arr[i]):
      print(i)



