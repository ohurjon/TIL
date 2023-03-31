
for i in range(0, 4):
    print("bit", i, ": ", end="")
    for n in range(0, 16):
        if n & (1 << i):
            print(n, sep=" ", end=" ")
    print("\n")
