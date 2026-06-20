N = int(input())
arr = list(map(int, input().split()))

K = 3
X = 5

left = 0
right = N - 1

while right - left + 1 > K:

    if abs(arr[left] - X) > abs(arr[right] - X):
        left += 1
    else:
        right -= 1

for i in range(left, right + 1):
    print(arr[i], end=" ")