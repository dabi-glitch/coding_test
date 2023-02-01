def binary_search(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if array[mid] == target:
    return mid

  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  
  elif array[mid] < target:
    return binary_search(array, target, mid+1, end)
  
N = int(input())
array = list(map(int, input().split()))
array.sort() #이진 탐색을 수행하기 위해서 정렬 수행행

M = input()
array1 = list(map(int, input().split()))

check = []

for i in array1:
  target = i
  result =  binary_search(array, target, 0, N-1)
  if result == None:
    check.append("No")
  else:
    check.append("Yes")

print(check)