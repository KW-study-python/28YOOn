N = int(input())

dancing = {"ChongChong"}

for _ in range(N):
    A, B = input().split()

    if A in dancing:
        dancing.add(B)

    if B in dancing:
        dancing.add(A)

print(len(dancing))
