import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

for i in arr1:
    if arr.find(i) == 1:
        print(1)
    else:z
    print(arr.find(i))