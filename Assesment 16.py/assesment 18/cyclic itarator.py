T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    arr = list(map(int, input().split()))
    it = iter(arr)
    total = 0
    for _ in range(k):
        try:
            total += next(it)
        except StopIteration:
            it = iter(arr)
            total += next(it)
    print(total)