file = open("Codingal.txt", "r")
print(file.read())
file.close()

file = open("Codingal.txt", "r")
print("\n Reading line by line \n")
print(file.read(7))
file.close()

file = open("Codingal.txt", "a")
file.write(" This is the new line added.")
file.close()