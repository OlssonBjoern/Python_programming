filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename2 = "pi_million_digits.txt"

with open(filename2) as f_obj:
    lines2 = f_obj.readlines()

# Print first 50 digits to not need 1,000,000 digits in the terminal
pi_string2 = ""

for line in lines2:
    pi_string2 += line.strip()

print(pi_string2[:52])
print(len(pi_string2))