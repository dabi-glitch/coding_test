vo_ca = list(input()) #소문자로 주어짐
arr = [] #a~z list
ind_list = []

for i in range(97,123): #a~z까지 들어있는 list 생성
  arr.append(chr(i))

for j in arr:
  if j in vo_ca: 
    ind_list.insert(arr.index(j), vo_ca.index(j))
  else :
    ind_list.insert(arr.index(j), -1)

for ind in ind_list:
  print(ind, end=" ")
 