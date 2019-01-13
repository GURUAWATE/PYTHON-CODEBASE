import csv
from datetime import datetime

path = "Google_Stock.csv"

file = open(path, newline = '')

reader = csv.reader(file)
headers = next(reader)
dataset = []

for row in reader:

    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high_price = float(row[2])
    low_price = float(row[3])
    close_price = float(row[4])
    volume_stock = int(row[5]) 
    adj_close_price = float(row[6])
    
    dataset.append([date, open_price, high_price, low_price, close_price, volume_stock, adj_close_price])

write_path = "Google_ruturns_daily.csv"

file = open(write_path, "w+") # open file in overwrite mode

writer = csv.writer(file)

# Write the header row
writer.writerow(["Date", "Return", "% of Return"])

# Let's write the logic for calculating daily return 

for i in range(len(dataset) - 1):
    
    day_data = dataset[i]
    day_before_data = dataset[i + 1]
    
    # CSV files are arranged in newest first (stack) manner, Hence yesterday's data will be at current index + 1 
    
    date = day_data[0].strftime('%d/%m/%Y')
    
    # index '-1' takes you to last element in the list, because it allows wrap-around
    
    returns = day_data[-1] - day_before_data[-1]
        
    per_ret = 100 * (returns / day_before_data[-1] )
    
    writer.writerow([date, returns, per_ret])
    
print("\nCheck the file named: ", write_path)