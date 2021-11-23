# 1.10.5
A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print ("Это нормально")
elif A > H:
    print ("Недосып")
else:
    print ("Пересып")

# 1.10.6
A = int(input())
if (A % 4 == 0 and A % 100 != 0) or A % 400 == 0:
    print ("Високосный")
else:
    print ("Обычный")

# 1.12.1
a, b, c = int(input()), int(input()), int(input())
p = (a + b + c)/2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print (float(S))

# 1.12.2
a = int(input())
if -15 < a <=12 or 14 < a < 17 or a >= 19:
    print (True)
else:
    print (False)

# 1.12.3
ch1 = float(input())
ch2 = float(input())
oper = input()
if oper == "+":
    print(ch1 + ch2)
elif oper == "-":
    print(ch1-ch2)
elif oper == "/":
    if ch2 != 0.0:
        print(ch1 / ch2)
    else:
        print("Деление на 0!")
elif oper == "*":
    print (ch1 * ch2)
elif oper == "mod":
    if ch2 != 0.0:
        print(ch1 % ch2)
    else:
        print("Деление на 0!")
elif oper == "pow":
    print(ch1 ** ch2)
elif oper == "div":
    if ch2 != 0.0:
        print(ch1 // ch2)
    else:
        print("Деление на 0!")

# 1.12.4
f = input()
if f == "треугольник":
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif f == "прямоугольник":
    a, b = int(input()), int(input())
    S = a * b
    print(S)
elif f == "круг":
    r = int(input())
    S = 3.14 * r ** 2
    print(S)

# 1.12.5
a, b, c = int(input()), int(input()), int(input())
if b <= a >= c and a >= b <= c:
    print(str(a) + "\n" + str(b) + "\n" + str(c))
elif c <= a >= b and a >= c <= b:
    print(str(a) + "\n" + str(c) + "\n" + str(b))
elif a <= b >= c and b >= a <= c:
    print(str(b) + "\n" + str(a) + "\n" + str(c))
elif c <= b >= a and b >= c <= a:
    print(str(b) + "\n" + str(c) + "\n" + str(a))
elif b <= c >= a and c >= b <= a:
    print(str(c) + "\n" + str(b) + "\n" + str(a))
elif a <= c >= b and c >= a <= b:
    print(str(c) + "\n" + str(a) + "\n" + str(b))

# 1.12.6
w = int(input())
if w % 10 == 0 or (w + 5) % 10 == 0 or (w + 4) % 10 == 0 or (w + 3) % 10 == 0 or (w + 2) % 10 == 0 or (w + 1) % 10 == 0:
    print(w, "программистов")
elif (w + 89) % 100 == 0 or (w + 88) % 100 == 0 or (w + 87) % 100 == 0 or (w + 86) % 100 == 0 or (w + 85) % 100 == 0 or (w + 84) % 100 == 0 or (w + 83) % 100 == 0 or (w + 82) % 100 == 0 or (w + 81) % 100 == 0:
    print(w, "программистов")
elif (w + 9) % 10 == 0:
    print(w, "программист")
elif (w + 8) % 10 == 0 or (w + 7) % 10 == 0 or (w + 6) % 10 == 0:
    print(w, "программиста")

# 1.12.7
w = list(input())
x1 = []
x2 = []
x1.append(int(w[0]))
x1.append(int(w[1]))
x1.append(int(w[2]))
x2.append(int(w[3]))
x2.append(int(w[4]))
x2.append(int(w[5]))
if sum(x1) == sum(x2):
    print("Счастливый")
else:
    print("Обычный")

# 2.1.11
w = int(input())
s = 0
while w != 0:
    s += w
    w = int(input())
print(s)

# 2.1.12
a, b = int(input()), int(input())
if a == b:
    print(a)
else:
    c = 1
    while c != (a * b):
        if c % a == 0 and c % b ==0:
            print(c)
            break
        else:
            c += 1
        if c == a * b:
            print(a * b)

# 2.2.4
s = 0
while s <= 100:
    s = int(input())
    if s < 10:
        continue
    elif s > 100:
        break
    else:
        print(s)

# 2.3.3
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if c == d:
    print("\t", c)
else:
    for x2 in range(c, d + 1):
        print("\t", x2, end="")
        if x2 == d:
            print('')
for x in range(a, b + 1):
    print(x, end="\t")
    for x1 in range(c, d + 1):
        print(x * x1, end="\t")
        if x1 == d:
            print('')

# 2.3.7
a, b = int(input()), int(input())
s = 0
w = 0
if a % 3 == 1:
    a += 2
elif a % 3 == 2:
    a += 1
for a in range(a, b + 1, 3):
    s += a
    w += 1
print(s / w)

# 2.4.3
s = input()
s1 = s.upper()
w = len(s1)
w1 = s1.count("G")
w2 = s1.count("C")
print(((w1 + w2)/w) * 100)

# 2.4.7
s = input()
w = len(s)
a = 0
k = 1
x = ""
for i in range(w):
    if i != w - 1:
        if s[a] == s[a + 1]:
            k += 1
            a += 1
            continue
        else:
            x += str(s[a]) + str(k)
            k = 1
            a += 1
    else: x += str(s[a]) + str(k)
print(x)

# 2.5.9
s = [int(i) for i in input().split()]
print(sum(s))

# 2.5.10
s = [int(i) for i in input().split()]
w = len(s)
x = ""
if w == 1:
    print(str(s[0]))
else:
    for i in range(w):
        if i == 0:
            x += (str(s[1] + s[-1]) + " ")
        elif i == w - 1:
            x += (str(s[-2] + s[0]) + "")
        else:
            x += (str(s[i - 1] + s[i + 1]) + " ")
    print(x)

# 2.5.11
s = [int(i) for i in input().split()]
s = sorted(s)
w = len(s)
x = ""
if w == 1:
    print()
else:
    for i in range(w):
        if i == w - 1:
            if x == "":
                print()
            else:
                x = x[0:-1]
                print(x)
        elif i != 0 and s[i] == s[i - 1] :
            continue
        elif s[i] == s[i + 1]:
            x += (str(s[i]) + " ")

# 2.6.7
x = [int(input())]
while sum(x) != 0:
    x.append(int(input()))
w = []
for i in (x):
    w.append(i * i)
print(sum(w))

# 2.6.8
s = int(input())
w = 1
x = ""
for i in range(s):
    x += (str(w) + " ")
    if w == x.count(str(w)):
        w += 1
print(x[0:-1])

# 2.6.9 - 1
s = [int(i) for i in input().split()]
x = int(input())
w = []
for i in range (len(s)):
    if x == s[i]:
        w.append(i)
if w == []:
    print('Отсутствует')
else:
    print(*w)

# 2.6.9 - 2
l = [int(i) for i in input().split()]
x = int(input())
if not x in l:
    print('Отсутствует')
for i in range(len(l)):
    if l[i] == x:
        print(i, end=' ')

# 2.6.10 - 1
a = []
while True:
    x = input()
    if x != "end":
        w = [int(i) for i in x.split()]
        a.append(list(w))
    else:
        break
if len(a[0]) == 1 and len(a) == 1:
    print(int(str(a[0][0])) * 4)
elif len(a[0]) > 1 and len(a) == 1:
    for j in range(len(a[0])):
        if j == 0:
            print(int(a[0][0]) + int(a[0][0]) + int(a[0][-1]) + int(a[0][1]), end=' ')
        elif 0 < j < (len(a[0]) - 1):
            print(int(a[0][j]) + int(a[0][j]) + int(a[0][j - 1]) + int(a[0][j + 1]), end=' ')
        elif j == (len(a[0]) - 1):
            print(int(a[0][j]) + int(a[0][j]) + int(a[0][j - 1]) + int(a[0][0]), end=' ')
elif len(a[0]) == 1 and len(a) > 1:
    for i in range(len(a)):
        if i == 0:
            print(int(a[-1][0]) + int(a[1][0]) + int(a[0][0]) + int(a[0][0]))
        elif 0 < i < (len(a) - 1):
            print(int(a[i - 1][0]) + int(a[i + 1][0]) + int(a[i][0]) + int(a[i][0]))
        elif i == (len(a) - 1):
            print(int(a[i - 1][0]) + int(a[0][0]) + int(a[-1][0]) + int(a[-1][0]))
else:
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i  == 0:
                ni = -1
            elif i == len(a) - 1:
                ni = 0
            else:
                ni = i
            if j == 0:
                nj = -1
            elif j == len(a[0]) - 1:
                nj = 0
            else:
                nj = j
            if i == 0 and j == 0:
                print(int(a[ni][j]) + int(a[i + 1][j]) + int(a[i][nj]) + int(a[i][j + 1]), end=' ')
            elif i == 0 and 0 < j < (len(a[0]) - 1):
                print(int(a[ni][j]) + int(a[i + 1][j]) + int(a[i][j-1]) + int(a[i][j + 1]), end=' ')
            elif i == 0 and j == (len(a[0]) - 1):
                print(int(a[ni][j]) + int(a[i + 1][j]) + int(a[i][j - 1]) + int(a[i][nj]), end=' ')
            elif 0 < i < (len(a) - 1) and j == 0:
                print(int(a[i + 1][j]) + int(a[i - 1][j]) + int(a[i][nj]) + int(a[i][j + 1]), end=' ')
            elif 0 < i < (len(a) - 1) and 0 < j < (len(a[0]) - 1):
                print(int(a[i - 1][j]) + int(a[i + 1][j]) + int(a[i][j - 1]) + int(a[i][j + 1]), end=' ')
            elif 0 < i < (len(a) - 1) and j == (len(a[0]) - 1):
                print(int(a[i - 1][j]) + int(a[i + 1][j]) + int(a[i][j - 1]) + int(a[i][nj]), end=' ')
            elif i == (len(a) - 1) and j == 0:
                print(int(a[i - 1][j]) + int(a[ni][j]) + int(a[i][-1]) + int(a[i][j + 1]), end=' ')
            elif i == (len(a) - 1) and 0 < j < (len(a[0]) - 1):
                print(int(a[i - 1][j]) + int(a[ni][j]) + int(a[i][j - 1]) + int(a[i][j + 1]), end=' ')
            elif i == (len(a) - 1) and j == (len(a[0]) - 1):
                print(int(a[i - 1][j]) + int(a[ni][j]) + int(a[i][j - 1]) + int(a[i][nj]), end=' ')
        print()

# 2.6.10 - 2
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()

# 2.6.11
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
z = 'верх'
c = 1
h = 0
for i in range(n // 2):
    if z == 'верх':
        for i in range(h, n - 1 - h):
            a[h][i] = c
            c += 1
        z = 'право'
    if z == 'право':
        for i in range(h, n - 1 - h):
            a[i][n - 1 - h] = c
            c += 1
        z = 'низ'
    if z == 'низ':
        for i in range(n - 1 - h, h, -1):
            a[n - 1 - h][i] = c
            c += 1
        z = 'лево'
    if z == 'лево':
        for i in range(n - 1 - h, h, - 1):
            a[i][h] = c
            c += 1
        z = 'верх'
        h += 1
if n % 2 == 1:
    a[n // 2][n // 2] = n * n
for i in range(0, n):
    print(*a[i])

# 3.1.8
def f (x):
    if x <= -2:
        x = 1 - (x + 2)**2
    elif -2 < x <= 2:
        x = (x / 2) * -1
    elif 2 < x:
        x = (x - 2)**2 + 1
    return x

# 3.1.9
lst = [1, 2, 3, 4, 5, 6, 8]
def modify_list(lst):
    z = []
    for i in lst:
        if i % 2 == 0:
            z.append(i // 2)
    lst.clear()
    lst.extend(z)
modify_list(lst)
print(lst)

# 3.2.5
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]

# 3.2.6
s = input()
s = s.lower()
s = [i for i in s.split()] # s = s.split()
# можно и так s = input().lower().split()
d = {}
print(s)
for i in (s):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i, j in d.items():
    print(i, j)

# 3.2.7
# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
s = int(input())
z = {}
for i in range(s):
    x = int(input())
    if x in z:
        print(z[x])
    else:
        z[x] = f(x)
        print(f(x))

# 3.4.2
s = open("s:\\temporary files\\dataset_3363_2.txt")
s1 = s.readline()
s1 = list(s1)
s.close()
z = ""
z_str = ""
z_int = ""
def r():
    global z_int
    z_int = int(z_int)
    global z_str
    global z
    z += z_str * z_int
    z_int = ""
for i in s1:
    if i < "A":
        z_int += i
    else:
        if z_str == "":
            z_str = i
        else:
            r()
            z_str = i
r()
s = open("s:\\temporary files\\03.11.txt", 'w')
s.write(z)
s.close()

# 3.4.3
d = {}
with open("s:\\temporary files\\dataset_3363_3.txt") as s:
    for line in s:
        line = line.lower()
        line = line.split()
        for i in line:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
o = 0
p = []
for v in d.values():
    if v > o:
        o = v
for k, v in d.items():
    if v == o:
        l = k + " " + str(v)
        p.append(l)
u = p[0]
for i in p:
    if i < u:
        u = i
s = open("s:\\temporary files\\19.11.txt", 'w')
s.write(u)
s.close()

# 3.4.4
d = {}
w = ''
m = 0
f = 0
r = 0
c = 0
with open("u:\\Temporary file\\dataset_3363_4.txt") as s:
    for line in s:
        line = line.split(';')
        d[line[0]] = line[1:4]
    for v in d.values():
        w += str((int(v[0]) + int(v[1]) + int(v[2])) / 3) + "\n"

for v in d.values():
    m += int(v[0])
    f += int(v[1])
    r += int(v[2])
    c += 1
w += str(m / c) + " "
w += str(f / c) + " "
w += str(r / c)
s = open("u:\\Temporary file\\16.01.txt", 'w')
s.write(w)
s.close()

# 3.5.2
import math
r = float(input())
p = 2 * math.pi * r
print(p)

# 3.5.3
import sys
s = sys.argv
for v in s:
    if v != s[0]:
        print(v + " ")

# 3.6.2
import requests
s = open("u:\\Temporary file\\\dataset_3378_2.txt")
url = s.readline().strip()
s.close()
r = requests.get(url)
r = r.text
r = r.splitlines()
r = str(len(r))
s = open("u:\\Temporary file\\26.01.txt", 'w')
s.write(r)
s.close()

# 3.6.3
import requests
s = open("u:\\Temporary file\\dataset_3378_3.txt")
url = s.readline().strip()
s.close()
r = requests.get(url)
l = r.text
u = 'https://stepic.org/media/attachments/course67/3.6.3/'
while True:
    if l[0] == 'W' and l[1] == 'e':
        break
    else:
        url = u + l
        r = requests.get(url)
        l = r.text
s = open("u:\\Temporary file\\27.01.txt", 'w')
s.write(l)
s.close()

# 3.7.1
d = {}
s = int(input())
for i in range (s):
    res = input()
    res = res.split(';')
    if res[0] in d:
        d[res[0]][0] += 1
    else:
        d[res[0]] = [1, 0, 0, 0, 0]
    if res[2] in d:
        d[res[2]][0] += 1
    else:
        d[res[2]] = [1, 0, 0, 0, 0]
    if int(res[1]) > int(res[3]):
        d[res[0]][1] += 1
        d[res[0]][4] += 3
        d[res[2]][3] += 1
    elif int(res[1]) < int(res[3]):
        d[res[2]][1] += 1
        d[res[2]][4] += 3
        d[res[0]][3] += 1
    elif int(res[1]) == int(res[3]):
        d[res[0]][2] += 1
        d[res[2]][2] += 1
        d[res[0]][4] += 1
        d[res[2]][4] += 1
for key, value in d.items():
    print((key + ':'), *value, end='\n')

# 3.7.2
w1, w2, q1, q2 = input(), input(), input(), input()
x, x1 = "", ""
for i in q1:
    n = 0
    for j in w1:
        if i == j:
            x += w2[n]
        else:
            n += 1
for i in q2:
    n = 0
    for j in w2:
        if i == j:
            x1 += w1[n]
        else:
            n += 1
print(x, '\n' + x1)

# 3.7.3
s = int(input())
a, b, c = [], [], []
for i in range(s):
    a.append(input().lower())
s1 = int(input())
for i in range(s1):
    v = (input().lower().split())
    for j in v:
        b.append(j)
for i in b:
    if i in a:
        True
    else:
        if i in c:
            True
        else:
            c.append(i)
            print(i)

# 3.7.4
s = int(input())
k1 = 0
k2 = 0
for i in range(s):
    n = (input().split())
    if n[0] == "север":
        k2 += int(n[1])
    elif n[0] == "юг":
        k2 -= int(n[1])
    elif n[0] == "восток":
        k1 += int(n[1])
    elif n[0] == "запад":
        k1 -= int(n[1])
print(k1, k2)

# 3.7.5
m = ''
d = {}
for i in range(1, 12):
    d[i] = [0, 0]
with open("s:\\temporary files\\dataset_3380_5.txt") as s:
    for line in s:
        line = line.split()
        if int(line[0]) in d:
            d[int(line[0])][0] += int(line[2])
            d[int(line[0])][1] += 1
for i in range(1, 12):
    if d[i][0] == 0:
        m += str(i)
        m += ' '
        m += " - \n"
    else:
        m += str(i)
        m += ' '
        m += str(d[i][0] / d[i][1])
        m += '\n'
s = open("s:\\temporary files\\31.01.txt", 'w')
s.write(m)
s.close()