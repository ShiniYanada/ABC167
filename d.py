n, k = list(map(int, input().split()))
trans = list(map(int, input().split()))
trans = [-1] + trans
dest = 1
seen = [False] * (n+1)
start = 0
output = 0
t = []
for _ in range(k):
  dest = trans[dest]
  if seen[dest]:
    for i, x in enumerate(t):
      if x == dest:
        start = i
    break
  seen[dest] = True
  t.append(dest)
if len(t) < k:
  s = t[start:]
  output = s[(k - len(t[:start]) - 1) % len(s)]
else:
  output = t[k-1]
print(output)
  
