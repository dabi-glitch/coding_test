sentance = input().strip()

if sentance == '':
  print(0)
else:
  cnt = sentance.count(' ')
  print(cnt+1)