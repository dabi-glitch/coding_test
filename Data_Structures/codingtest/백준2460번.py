arr = []
def repeat(x):
  for i in range(10):
    a, b = map(int, input().split())
    x = x - a + b
    arr.append(x)

result = repeat(0)
print(max(arr))

