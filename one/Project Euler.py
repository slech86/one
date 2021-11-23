s=[]
for x in  range (1, 1000):
    if x %3 == 0 or x %5 == 0:
        s.append(x)
print(sum(s))

a=[x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(a))


_s = 0
s1 = 0
s2 = 1
x = []
while _s <= 4000000:
    _s = s1 + s2
    if _s %2 == 0:
        x.append(_s)
    s1 = s2
    s2 = _s
print(sum(x))




