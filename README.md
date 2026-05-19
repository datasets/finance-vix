<a className="gh-badge" href="https://datahub.io/core/finance-vix"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Finance VIX

CBOE Volatility Index (VIX) time-series dataset including daily open, close,
high and low, covering January 1990 to present. The CBOE Volatility Index (VIX)
is a key measure of market expectations of near-term volatility conveyed by
S&P 500 stock index option prices introduced in 1993.

## Data

From the [CBOE VIX historical data page][historical]:

> In 1993, the Chicago Board Options Exchange® (CBOE®) introduced the CBOE
> Volatility Index®, VIX®, and it quickly became the benchmark for stock market
> volatility. It is widely followed and has been cited in hundreds of news
> articles in the Wall Street Journal, Barron's and other leading financial
> publications. Since volatility often signifies financial turmoil, VIX is
> often referred to as the "investor fear gauge".
>
> VIX measures market expectation of near term volatility conveyed by stock
> index option prices. The original VIX was constructed using the implied
> volatilities of eight different OEX option series so that, at any given time,
> it represented the implied volatility of a hypothetical at-the-money OEX
> option with exactly 30 days to expiration.
>
> The New VIX still measures the market's expectation of 30-day volatility, but
> in a way that conforms to the latest thinking and research among industry
> practitioners. The New VIX is based on S&P 500 index option prices and
> incorporates information from the volatility "skew" by using a wider range of
> strike prices rather than just at-the-money series.

[historical]: https://www.cboe.com/tradable_products/vix/vix_historical_data/

### Data quirks

- **Early OHLC data (through 06/11/2004):** The first 506 rows of `vix-daily.csv`
  have identical OPEN, HIGH, LOW, and CLOSE values. CBOE only recorded daily
  closing values before mid-2004; the open/high/low fields are filled with the
  close value for those dates.
- **Monthly data:** `vix-monthly.csv` is derived from the daily file on every
  run. Each row is the last trading day's close for that calendar month.

## Development

This is a simple pipeline where the only requirement is to have `curl` and `make`. You can get the data by running the following command locally:

```bash
make
```

The daily data is fetched from:
`https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`

## License

No obvious statement on [historical data page][historical]. Given size and
factual nature of the data and its source from a US company would imagine this
was public domain and as such have licensed the Data Package under the Public
Domain Dedication and License (PDDL).
