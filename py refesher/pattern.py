# basic star pattern
print("Star Pattern\n")
for i in range(1,10):
    for j in range(i):
        print("*", end=" ")
    print("\n")
# inverted start pattern
print("Inverted Star Pattern\n")
for i in range(10, 1 ,-1):
    for j in range(i, 1, -1):
        print("*", end=" ")
    print("\n")