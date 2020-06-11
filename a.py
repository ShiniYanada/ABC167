s = input()
t = input()
if (s == t[0:len(s)] and len(s) + 1 == len(t)):
  print('Yes')
else:
  print('No')
