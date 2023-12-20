import os

# open the file in readonly mode
f = open('file.txt', 'r')


# read and display the entire file
s = f.read()
print(s)


# reset file position to start
# read and display the first line of the file
f.seek(0)
s = f.readline()
print(s)


# read one-by-one and display 4 characters from the 11th character of the file
f.seek(11)
for i in range(4):
    s = f.read(1)
    print(s, end='')
print()

# get number of characters of the file
# reset file position to the end and get file position value
f.seek(0, os.SEEK_END)
n = f.tell()
print("The file has {} characters".format(n))

