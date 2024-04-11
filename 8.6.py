n = int(input())
n1 = n
while n != 0:
    n -= 1
    print(n * ' ' + (n1 - n) * '*')