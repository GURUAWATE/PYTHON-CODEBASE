path = "Google_Stock.csv"

line = [line for line in open(path)] # Using list comprehension for creating a list of strings

# Let's print first 20 lines

for i in range(0,21):
    print("\n", line[i])

print("\nThis method is less-readable hence not highly operable.")

print(80*"--")
print(80*"--")

print("\nNow, let's separate values in each string via tokenizing")

dataset = [line.strip().split(',') for line in open(path)]

# strip() will remove any leading or trailing spaces
# split(',') will tokenize our values by separating them from ',' and convert a string into a list
# Hence, now 'dataset' is a list of lists

# Let's print first 20 lines

for i in range(0,21):
    print("\n", dataset[i])

print("\nHere, values are distinguished and have become operable.")

print("\nSometimes, the values may contain commas and does not necessarily make them a different value altogether,\nHence splitting them into different values may be incorrect,")
print("\n\t For that purpose you may use CSV module.")