t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b =[]
for i in range(len(a)):
    if i%2 == 0:
        b.append(a[i])  
    else:
        b.append(-a[i+1])
current = b[0]
max_energy = b[0]
for i in range(1,len(b)):
    current = max(b[i], current+b[i])
    max_energy = max(max_energy, current)
print(max_energy)

