from collections import Counter
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
  arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

#산술평균
print(int(round(sum(arr)/n,0)))

#중앙값
print(arr[n//2])

#최빈값
cnt = Counter(arr)
value = cnt.most_common()
maxium = value[0][1]
mods = []

for num in value:
  if num[1] == maxium:
    mods.append(num[0])

if len(mods) >= 2:
  print(mods[1])
else:
  print(mods[0])


#범위
print(max(arr) - min(arr))