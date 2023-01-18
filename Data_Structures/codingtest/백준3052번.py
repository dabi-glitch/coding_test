a = []
result = []
for _ in range(10):
  num = int(input())
  a.append(num%42)

for j in a:
    if j not in result:
        result.append(j)


print(len(result))