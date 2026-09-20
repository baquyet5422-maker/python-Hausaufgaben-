from math import gcd
with open("PHANSO.INP", "r") as f:
    data = f.read().split()
a, b, c, d = map(int, data)
t = gcd(a, c)
m = (b * d) // gcd(b, d)
g = gcd(t, m)
with open("PHANSO.OUT", "w") as f:
    f.write(str(t // g) + " " + str(m // g))
