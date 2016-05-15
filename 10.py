a = '1'
i = 1

while i <= 30:
    j = 0
    b = ''
    while j < len(a):
        k = j
        while k < len(a) and a[k] == a[j]:
            k += 1
        b = b + str(k - j) + a[j]
        j = k
    a = b
    print("%d:" % i)
    print(a)
    print(len(a))
    i += 1