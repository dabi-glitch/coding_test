voca = input().upper()
voca_list = list(set(voca))
cnt = []

for i in voca_list:
  cnt.append(voca.count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(voca_list[(cnt.index(max(cnt)))])