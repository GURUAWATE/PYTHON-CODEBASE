import csv
from datetime import datetime

path = "Google_Stock.csv"

file = open(path, newline = '')

# headers are ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# let's read and convert these string values into their appropriate individual types.

reader = csv.reader(file)
headers = next(reader)
dataset = []

for row in reader:

    date = datetime.strptime(row[0], '%m/%d/%Y') # pass in the string & it's format
    open_price = float(row[1]) # we may create conflict, if we used 'open' as variable name, because it is already a python function.
    high_price = float(row[2])
    low_price = float(row[3])
    close_price = float(row[4])
    volume_stock = int(row[5]) # volume is number denoting total number trades for that stock and it's a whole number, hence we convert it to int.
    adj_close_price = float(row[6])
    
    # Add these converted values to the dataset list.
    dataset.append([date, open_price, high_price, low_price, close_price, volume_stock, adj_close_price])

# Let's print first 20 lines
print("\n", headers)
for i in range(0,20):
    print("\n", dataset[i])
    
print("\n Notice that the values do not contain any string_quotes (''), Meaning, that they have been successfully converted to their respective types.\n ")

data = dataset[1] # fetch a single row
print("[", type(data[0]), ",", type(data[1]), ",", type(data[2]), ",", type(data[3]), ",", type(data[4]), ",", type(data[5]), ",", type(data[6]), "]")

print("\n The date is still not readable, we will format it when we write into CSV file, Let's do that next...")