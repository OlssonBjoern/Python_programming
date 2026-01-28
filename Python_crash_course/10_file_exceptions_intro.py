filename = "pi_digits.txt"
# Reading inputs from file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# Printing line by line

with open(filename) as file_obj:
    for line in file_obj:
        print(line)

# Stripping newlines
with open(filename) as file_obj:
    for line in file_obj:
        print(line.rstrip())