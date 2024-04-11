N = int(input())
for i in range(2, N + 1):
    A = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            A.add(j)
            A.add(i // j)
    if len(A) == 0:
        print(i)