import csv

path = "Google_Stock.csv"

file = open(path, newline = '')
# newline = '', the empty value will ensure compatibility with all LF,CR or CRLF characters.

reader = csv.reader(file)

# Initially reader (which is similar to cursor in SQL) points to one item above the data, we may iterate or use next() to get the value

# Now let's get our first row, which is actually 'Headers' for each 'Columns' using next(), and also incrementing reader's pointer

headers = next(reader)

# Here, each row is already a list, which has already been stripped and separated

# Our variable 'dataset' now is a list of lists.
dataset = [row for row in reader]
# Now, reader has reached EOF, Hence we can not use print(next(reader))

# Let's print first 20 lines

print("\n", headers)
for i in range(0,20):
    print("\n", dataset[i])

print("\n We've achieved this with lesser efforts than before, But all the values are still in strings.")
print("\n We need to convert them into appropriate types, let's do this next..")