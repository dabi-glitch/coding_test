import heapq

n = int(input().rstrip()) #입력 횟수

heap = [int(input()) for _ in range(n)]

answer = 0

while True:

  if len(heap) > 1:
    print(heap)
    result = 0
    result = heapq.heappop(heap) + heapq.heappop(heap)
    answer += result
    heapq.heappush(heap, result)
    
  if len(heap) == 1:
    break

print(answer)
