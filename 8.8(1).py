s = '123456789'
for i in range(1, len(s) + 1):
    print(s[:i], '*', '8', '+', i, '=', int(s[:i]) * 8 + i)