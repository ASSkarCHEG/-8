s = '123456789'
for i in range(1, len(s) + 1):
    print(s[:i], '*', '9', '+', i + 1, '=', int(s[:i]) * 9 + (i + 1))