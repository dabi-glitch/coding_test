#그리디알고리즘 큰 수의 법칙

n, m, k = map(int, input().split()) #n배열의 길이 #m횟수 #k연속최대

arr = sorted(list(map(int, input().split())), reverse = True) #숫자 배열

result = 0


while m > 0:
  for a in range(k):
    result += arr[0]
    m -= 1
    if m <= 0:
      break
  
  if m <= 0:
    break
  else:
    result += arr[1]
    m -=1

print(result)