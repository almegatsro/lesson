file = open("Codingal.txt", "r")
print("Reading the first line...")
print(file.readline())
file.close()

file = open("Codingal.txt", "r")
print("\n Reading multitiple lines...")
print(file.readlines())
print(file.readlines())
print(file.readlines())
file.close()

file = open("Codingal.txt", "r")
print("\n looping through the lines...")
for line in file:
    print(line)
file.close()