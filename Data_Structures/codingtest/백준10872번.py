n = int(input())
result = n

if n == 0:
  result = 1

else :
  for i in range(1,n):
    result = result * (n-i)

print(result)