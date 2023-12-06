import sys

# print number of command arguments
print("Number of command arguments: ", len(sys.argv))

# print first argument
print("First argument: ", sys.argv[0])

# print all arguments
for i, arg in enumerate(sys.argv):
    print("Argument {}: {}".format(i, arg))
