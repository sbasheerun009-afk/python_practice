s = 'aabbccc'
s = s.replace('c',' ',1)
freq = {}
for ch in s:
    if ch in freq:
            freq[ch] += 1
    else:
            freq[ch] = 1
vals = []
for v in freq.values():
       freq[ch] -= 1
       if v > 0:
             vals.append(v)
       if len(set(vals)) == 1:
              print("yes")
              break
       freq[ch] += 1
else:
       if freq(set.values()):
              print("yes")
       else:
              print("no")
              
 
'''              
s = ['apple, mango ,apple, orange, mango, banana, kiwi']
freq = {}
count = 0
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        count += 1
        print(count)
print(freq)'''
'''n = int(input())
s = input().split()
unique_fruits = set(s)
sorted_fruits = sorted(unique_fruits)
print(*sorted_fruits)'''
m = int(input())
a = set(input().split())
n = set(input().split())
b = input().split()
print(a.intersection(b))
