n = int(input())
total = 0
counter = 0
while n != 0:
    total += 1
    counter += n
    n = int(input())
print(counter / total)