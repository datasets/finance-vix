<a className="gh-badge" href="https://datahub.io/core/finance-vix"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Finance VIX

CBOE Volatility Index (VIX) time-series dataset including daily open, close,
high and low. The CBOE Volatility Index (VIX) is a key measure of market
expectations of near-term volatility conveyed by S&P 500 stock index option
prices introduced in 1993.

## Data

From the [VIX FAQ][faq]:

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

[faq]: http://www.cboe.com/micro/vix/faq.aspx

## Development

This is a simple pipeline where the only requirement is to have `curl` and `make`. You can get the data by running the following command locally:

```bash
make
```

## License

No obvious statement on [historical data page][historical]. Given size and
factual nature of the data and its source from a US company would imagine this
was public domain and as such have licensed the Data Package under the Public
Domain Dedication and License (PDDL).

[historical]: https://www.cboe.com/tradable_products/vix/vix_historical_data/
