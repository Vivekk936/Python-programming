from collections import Counter

t = int(input())

for _ in range(t):
    s = input().strip()

    freq = Counter(s)

    ans = 0
    for cnt in freq.values():
        ans += cnt // 2

    print(ans)