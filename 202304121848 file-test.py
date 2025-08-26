f = open("test.txt", "r")
print(f)
print(f.read())
print(f.readline())
print(f.readlines())

f = open("test.txt", "a")
f.write("\nFLAG\nFLAG\nFLAG")
f.close()
f = open("test.txt", "r")
print(f.read())

f = open("test.txt", "w")
f.write("NO FLAGS!")
f.close()
f = open("test.txt", "r")
print(f.read())


'''
f = open("file_name", "r")
print(f.read())

f = open("demofile1.txt", "a") # Append to an existing file
f.write("The file will include more text..")
f.close()

f = open("demofile2.txt", "w") # Creating and writing to a new file
f.write("demofile2 file created, with this content in!")
f.close()

'''