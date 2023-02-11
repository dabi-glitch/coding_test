t = int(input()) #회의의 수
arr = [] #회의의 정보가 담긴 list
for i in range(t):
  time = list(map(int, input().split()))
  arr.append(time)

arr = sorted(arr, key = lambda x : (x[1],x[0]))
#끝나는 시간 순으로 정렬, 끝나는 시간이 같을 경우 시작 시간 순으로 정렬

cnt = 0
top = [0,0]

for i in arr:
  if i[0] >= top[1]: #전 회의의 끝 시간보다 시작시간이 크거나 같을 경우 회의 가능
    top = i
    cnt+=1

print(cnt)