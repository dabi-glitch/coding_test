from collections import Counter

n = int(input())
s_card = list(map(int, input().split()))
ex_counter = Counter(s_card)
s_card1 = sorted(set(s_card))
arr = []
m = int(input())
total_card = list(map(int, input().split()))

for i in total_card:
  start = 0
  end = len(s_card1) - 1
  result = False
  while start <= end:
    mid = (start+end)//2
    if s_card1[mid] == i:
      result = True
      break
    elif s_card1[mid] > i:
      end = mid-1
    elif s_card1[mid] < i:
      start = mid+1

  print(ex_couter[i] if result else 0, end = ' ')
