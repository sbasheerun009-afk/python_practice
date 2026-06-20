n = int(input())
ids = list(map(int, input().split()))

freq = {}

for i in ids:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

result = []

for key, value in freq.items():
    if value == 1:
        result.append(key)

result.sort()

print(*result)