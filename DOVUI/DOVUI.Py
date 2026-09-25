with open('DOVUI/DOVUI.INP', 'r') as file:
    n, k = map(int, file.readline().split())
    a = list(map(int, file.readline().split()))

l = 1
r = max(a)
ans: int = 0

while l <= r:
    t: int = 0
    m: int = (l + r) // 2
    for i in a:
        t += i // m
    if t >= k:
        l = m + 1
        ans = int(m)
    else:
        r = m - 1
with open('DOVUI/DOVUI.OUT', 'w') as file:
    file.write(str(ans))
