a, b, c  = map(int, input().split())


if a == b == c:
    print(10000 + a*1000)

elif a == b != c:
    s = a
    print(1000 + s*100)
    

elif a == c != b:
    s= a
    print(1000 + s*100)

elif b == c != a:
    s = b
    print(1000 + s*100)

elif a!=b!=c:
    if a>b and a>c:
        print(a*100)
    if b>a and b>c:
        print(b*100)
    if c>a and c>b:
        print(c*100)
        
