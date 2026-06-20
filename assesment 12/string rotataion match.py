
T = int(input())
s = list(map(int, input().split()))
n = len(s)
k = int(input())
for i in range(n-k-1,-1,-1):
    a = input().strip()
    b = input().strip()
    if len(a) != len(b):
        print("no")
        continue
    
    