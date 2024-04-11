s = '111111111'
for i in range(1, len(s) + 1):
    print(s[:i], '*', s[:i], '=', int(s[:i]) * int(s[:i]))