t = int(input())
for _ in range(t):
    s = input().strip()
    k = int(input())
    it = iter(s)
    password = " "
    for ch in range(k):
        try:
            password += next(it)
        except StopIteration:
            it = iter(s)
            password += next(it)
    print(password)
            


            
