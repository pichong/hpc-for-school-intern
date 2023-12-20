import os

# open file.txt file in read-only mode
f = open('file.txt', 'r')


# variable n represents the file pointer position
# of the next character to display
# initialize it at the end of the file
f.seek(0, os.SEEK_END)
n = f.tell()

while True:
    # decrement n by 1
    n = n - 1
    # set file pointer position
    f.seek(n)
    # read one character
    s = f.read(1)
    # display it
    print(s, end='')
    # break out of the loop when file position is at start
    if n == 0:
        break
