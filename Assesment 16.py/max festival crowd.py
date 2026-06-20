def max_visitors(A,N,K):
    window_sum = sum(A[:K])
    max_sum = window_sum
    for i in range(K,N):
        window_sum = window_sum+A[i] - A[i-K]
        max_sum = max(max_sum,window_sum)
    return max_sum
N,K = map(int,input().split())
A = list(map(int,input().split()))
print(max_visitors(A,N,K))

