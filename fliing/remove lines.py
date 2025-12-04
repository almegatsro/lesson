file1 = open('codingal.txt', 'r')
flie2 = open('codingalupdated.txt', 'w')
for line in file1.readlines():
        if not (line.startswith('Coding')):
            print(line)
            flie2.write(line)

file1.close()
flie2.close()