test_case = int(input())
num = int(input())
arr = []
num2 = [0]

while True :
    if (num // 2) != 1 or 0:
        arr.append(num%2)
        num = num//2
    elif (num // 2) == 1 :
        arr.append(num%2)
        num = num//2
        arr.append(num)
        break

for i in range(len(arr)):
    arr.append(arr.pop())

for i in range(len(arr)):
    if arr[i] == 0:
        num2[0] += 1
    else :
        print(num2[0],end=' ')
        num2[0] += 1
