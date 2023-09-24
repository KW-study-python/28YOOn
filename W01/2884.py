a, b  = map(int, input().split())


if b <45:
    if a == 0:
        a = 23
        b += 15
    else:
        a -= 1
        b += 15

    print(a, b)


elif b >= 45:
    a += 0
    b -= 45
    print(a,b)


