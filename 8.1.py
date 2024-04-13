n = int(input())
sr = 0
while n != -1:
    if n > sr:
        sr = n
    n = int(input())
print(sr)
