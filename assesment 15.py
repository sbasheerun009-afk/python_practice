#MAXIMUM SUM OF 3 NON OVERLAPING SUBARRAYS
n = int(input())
nums = [1,2,1,2,6,7,5,1]
k = int(input())
window_sum = []
current_sum = sum(nums[0:k])
window_sum.append(current_sum)
for i in range(k,n):
    current_sum = current_sum+nums[i]-nums[i-k]
    window_sum >= current_sum
for i in range(k,n):
   curr = curr + nums[i] - nums[i-k]
   window_sum.append(curr)
M = len(window_sum)

    # Step 2: Left side lo 0...i varaku best index
left = [0] * M
best = 0
for i in range(M):
    if window_sum[i] > window_sum[best]:
            best = i
            left[i] = best

    # Step 3: Right side lo i...end varaku best index
right = [0] * M
best = M - 1
for i in range(M-1, -1, -1):
    if window_sum[i] >= window_sum[best]: # >= lexico smallest kosam
            best = i
    right[i] = best

    # Step 4: Middle window fix chesi max total kanukko
    ans = []
    max_sum = 0

    for j in range(k, n - 2*k + 1):
        i = left[j - k]
        k = right[j + k]
        total = window_sum[i] + window_sum[j] + window_sum[k]

        if total > max_sum:
            max_sum = total
            ans = [i, j, k]

    print(*ans)


