file_1 = open("TestFile1.txt","r+")
file_2 = open("TestFile2.txt","r+")
for line in file_1 :
    if "\"" in line :
        line = line.replace("\"","\\\"")
        file_2.write(line)
a=file_2.readline()
print(a)
file_2.close()
file_1.close()
