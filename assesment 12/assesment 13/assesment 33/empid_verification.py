arr = list(map(int, input().split()))
l = int(input())
r = int(input())
count = 0
for i in range(l , r+1):
    digits = str(i)
    if len(digits)==len(set(digits)):
        count += 1
if count == 0:
    print("NouniqueNumber")
else:
    print(count)

