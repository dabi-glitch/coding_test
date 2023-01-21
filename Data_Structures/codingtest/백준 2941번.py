word = input()
cnt = 0

for i in range(len(word)):
  if i == 0:
    pass
  else:
    if word[i] in ['=']:
      if (word[i-1] in ['c','s']):
        cnt += 1
      elif (word[i-1] == 'z') and (word[i-2] != 'd'):
        cnt += 1
      elif word[i-1] == 'z' and word[i-2] == 'd':
        cnt += 2
    elif word[i] in ['-']:
      if word[i-1] in ['c','d']:
        cnt += 1
    elif word[i] in ['j']:
      if word[i-1] in ['l','n']:
        cnt += 1

result = len(word) - cnt

print(result)