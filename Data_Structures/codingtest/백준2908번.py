arr = list(input().split())
b = []
for i in arr:
  a = ''
  for j in (i[2],i[1],i[0]):
    a = a + j
  b.append(a)

print(max(b))