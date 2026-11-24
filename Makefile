all: data

.PHONY: data
data:
	curl -sL https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv -o data/vix-daily.csv
	python3 scripts/process.py
