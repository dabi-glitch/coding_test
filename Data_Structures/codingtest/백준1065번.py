numbers = int(input())
count= 0
for num in range(1,numbers+1): #N보다 작거나 같은 수를 num에 차례로 넣음
  if num < 100:
    count += 1
  else:
    num_list = list(map(int, str(num)))
    if num_list[1] - num_list[0] == num_list[2] - num_list[1]:
        count += 1

print(count)