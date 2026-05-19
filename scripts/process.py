import csv
from datetime import datetime

# Reformat daily dates from MM/DD/YYYY to YYYY-MM-DD
rows = []
with open('data/vix-daily.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        row[0] = datetime.strptime(row[0], '%m/%d/%Y').strftime('%Y-%m-%d')
        rows.append(row)
with open('data/vix-daily.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

# Derive monthly: last trading day close for each calendar month
monthly = {}
for row in rows:
    month = row[0][:7]  # YYYY-MM
    monthly[month] = (row[0], row[4])  # last row wins (data is ascending)
with open('data/vix-monthly.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Close'])
    for month in sorted(monthly):
        date, close = monthly[month]
        writer.writerow([date, close])
