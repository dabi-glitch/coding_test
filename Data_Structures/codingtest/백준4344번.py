c = int(input())

for i in range(c):
  arr = list(map(int, input().split()))
  count = 0
  avg = sum(arr[1:])/arr[0]
  for j in arr[1:]:
      if j > avg:
        count +=1
  score = (count/(arr[0])*100)
  print("{:.3f}".format(score)+"%")