N = int(input())
total = 0
for i in range(2, N + 1, 2):
    m = []
    for j in range(1, i):
        if i % j == 0:
            m.append(j)
    if sum(m) == i:
        total += 1
        m = []
    else:
        m = []
print(total)