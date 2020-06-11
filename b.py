a, b, c, k = list(map(int, input().split()))
sum = 0
if a > 0:
  if k - a > 0:
    sum += a
  else:
    sum += k
  k -= a
if b > 0 and k > 0:
  k -= b
if c > 0 and k > 0:
  sum -= k
print(sum)
