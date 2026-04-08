import pandas as pd

df = pd.read_csv("data/vix-daily.csv")
df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%Y")
df = df.sort_values("DATE")

# Take the last trading day of each month
monthly = df.groupby(df["DATE"].dt.to_period("M")).last().reset_index(drop=True)
monthly = monthly[["DATE", "CLOSE"]].rename(columns={"DATE": "Date", "CLOSE": "Close"})
monthly["Date"] = monthly["Date"].dt.strftime("%Y-%m-%d")
monthly["Close"] = monthly["Close"].round(2)

monthly.to_csv("data/vix-monthly.csv", index=False)
