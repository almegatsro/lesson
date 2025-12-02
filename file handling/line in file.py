file = open("codingal.txt", "r")
file.seek(0)
counter = 0
content = file.read()
colist = content.split("\n")

for i in colist:

    if i:
        counter + 1

print("Number of lines in the file:", counter)
file.close()