
def repeat(n) :
  if n <= 1:
    return n
  return repeat(n-1) + repeat(n-2)

n = int(input())
print(repeat(n))