n = int(input()) #자연수의 합
sum = 0

for i in range(1,n+1):
   sum += i
   if sum == n:
    print(i)
    break
   elif sum > n:
     print(i-1)
     break