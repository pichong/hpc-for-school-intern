
# assign character 'a'
c = 'a'
print(c)

# get int value of 'a'
v = ord(c)
print(v)

# get character following 'a'
d = chr(v + 1)
print(d)

# display characters from 'a' to 'z'
for i in range(ord('a'), ord('z')+1):
    print("{:3d} {}".format(i, chr(i)))

# print ASCII table
for i in range(0,256):
    print("{:3s}".format(chr(i)), end="")
    if i % 16 == 15:
        print()
