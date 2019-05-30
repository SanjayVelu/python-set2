a=int(input())
check=0
b=str(a)
for i in range(len(b)):
  check=check+int(b[i])**3
if (check==a):
  print("yes")
else:
  print("No")
