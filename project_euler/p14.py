def rek(n):
    global d
    d += 1
    if n > 1:
        if n % 2:
            return rek(3*n+1)
        return rek(n/2)
    return 1


a = []
for i in range(1, 1000001):
    d = 0
    rek(i)
    a.append([d, i])
print(max(a))
