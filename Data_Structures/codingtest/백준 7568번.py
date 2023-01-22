a = int(input())
num = 0
arr = []

for i in range(1,a+1):
  if i == 1:
    arr.append(1)
  elif i in [2,3,4,5,6,7]:
    arr.append(2)
  else:
      for i in range(2,a):
        if len(arr) >= a:
          break
        num += 6 * i
        for j in range(num, (num+6*i)):
          arr.append(i+1)
      
print(arr[a-1])