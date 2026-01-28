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

# Can save the file in a list to use it later.
# Otherwise it can only be used inside the "with" block of code

with open(filename) as f_obj:
    lines = f_obj.readlines()

    for line in lines:
        print(line.rstrip())