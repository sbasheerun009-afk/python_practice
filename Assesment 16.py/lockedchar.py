def longest_palindrome_length(s):
    n = len(s)
    longest = 1
    for i in range(n):
        l = r = i
        while l >= 0 and r < n and s[l]==s[r]:
            longest = max(longest, r - l + 1)
            l -= 1
            r += 1
        l = i
        r = i+1
        while l >= 0 and r < n and s[l]==s[r]:
            longest = max(longest, r - l + 1)
            l -= 1
            r += 1
    return longest
t = int(input())
for _ in range(t):
    s = input().strip()
    longest = longest_palindrome_length(s)
    print(len(s)-longest)
        




