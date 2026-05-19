all: data

.PHONY: data
data:
	curl -s https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv -o data/vix-daily.csv
	python3 -c "
import csv, sys
from datetime import datetime
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
"
