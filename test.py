import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print("\u001b[0m")
print("______")
print("\u001b[48;5;5m]")
print("     ")