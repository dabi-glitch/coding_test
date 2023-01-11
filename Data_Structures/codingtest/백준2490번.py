arr = 0

for i in range (3):
  arr[i] = list(map(int, input().split()))

for i in range (3):
  x,y = 0,0
  for j in range (4):
    if arr[i][j] == 0 :
      x = x + 1
    else :
      y = y + 1
  if x == 1 and y == 3 : print('A')
  elif x == 2 and y == 2 : print('B')
  elif x == 3 and y == 1 : print('C')
  elif x == 4 and y == 0 : print('D')
  else : print('E')