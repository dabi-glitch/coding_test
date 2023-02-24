
n = int(input())

result_num = [] #스택 수열
input_num = [] #1이상 n이하 정수
stack = []
answer = [] #부호 입력

for i in range(1,n+1):
  result_num.append(int(input()))
  input_num.append(i)

for i in range(len(result_num)):

  while len(stack) == 0 or stack[-1] != result_num[i]:
    if len(input_num) == 0 and stack[-1] != result_num[i]:
      print("NO")
      exit()
    
    stack.append(input_num[0])
    input_num.pop(0)
    answer.append("+")

  stack.pop()
  answer.append("-")
  
for i in range(len(answer)):
    print(answer[i])
