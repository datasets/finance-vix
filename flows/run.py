from dataflows import Flow, PackageWrapper, ResourceWrapper, validate
from dataflows import add_metadata, dump_to_path, load, set_type, printer


def rename(package: PackageWrapper):
    package.pkg.descriptor['resources'][0]['name'] = 'vix-daily'
    package.pkg.descriptor['resources'][0]['path'] = 'data/vix-daily.csv'
    yield package.pkg
    res_iter = iter(package)
    first: ResourceWrapper = next(res_iter)
    yield first.it
    yield from package


finance_vix = Flow(
    add_metadata(
        name="finance-vix",
        title= "VIX - CBOE Volatility Index",
        sources=[
            {
              "name": "CBOE VIX Page",
              "path": "http://www.cboe.com/micro/vix/historical.aspx",
              "title": "CBOE VIX Page"
            }
        ],
        licenses="PDDL-1.0",
        version="0.2.0",
        views=[
            {
              "name": "graph",
              "title": "VIX - CBOE Volatility Index",
              "specType": "simple",
              "spec": {"type": "line","group": "Date","series": ["VIXClose"]}
            }
        ]
    ),
    load(
        load_source='http://www.cboe.com/publish/ScheduledTask/MktData/datahouse/vixcurrent.csv',
        skip_rows=2,
        headers=['Date', 'VIXOpen', 'VIXHigh', 'VIXLow', 'VIXClose']
    ),
    set_type('Date', type='date', format='any'),
    rename,
    validate(),
    printer(),
    dump_to_path(),
)


if __name__ == '__main__':
    finance_vix.process()
