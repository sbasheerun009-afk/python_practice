N = int(input())
height = list(map(int, input().split()))

left = 0
right = N-1
water_max = 0

while left < right:
    length = min(height[left],height[right])
    width = right - left
    water_max = max(water_max,length*width)
    if height[right] < height[left]:
        left += 1
    else:
        right -= 1
print(water_max)