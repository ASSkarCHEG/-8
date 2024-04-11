N = int(input())
for i in range(2, N + 1, 2):
    m = []
    for j in range(1, i):
        if i % j == 0:
            m.append(j)
    if sum(m) == i:
        print(i)
        m = []
    else:
        m = []