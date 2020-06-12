n, m, x = list(map(int, input().split()))
lists = []
result_price = 0
existed = False
 
for i in range(n):
  lists.append(list(map(int, input().split())))
 
for i in range(1 << n):
  flag = True
  scores = [0] * m
  tmp_price = 0
  for j in range(n):
    if i & (1 << j):
      for k in range(m):
        scores[k] += lists[j][k+1]
      tmp_price += lists[j][0]
  for l in range(m):
    if scores[l] < x:
      flag = False
      break
  if flag and (result_price > tmp_price or result_price == 0):
    existed = True
    result_price = tmp_price
if existed:
  print(result_price)
else:
  print(-1)
