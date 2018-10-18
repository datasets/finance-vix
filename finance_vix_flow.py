import os

from dataflows import add_metadata, dump_to_path, load, set_type, validate
from dataflows import Flow, update_resource


def readme(fpath='README.md'):
    if os.path.exists(fpath):
        return open(fpath).read()


finance_vix = Flow(
    add_metadata(
        name="finance-vix",
        title= "VIX - CBOE Volatility Index",
        homepage= 'http://www.cboe.com/micro/VIX/',
        sources=[
            {
              "name": "CBOE VIX Page",
              "path": "http://www.cboe.com/micro/vix/historical.aspx",
              "title": "CBOE VIX Page"
            }
        ],
        licenses=[
            {
              "id": "odc-pddl",
              "path": "http://opendatacommons.org/licenses/pddl/",
              "title": "Open Data Commons Public Domain Dedication and License v1.0",
              'name': "open_data_commons_public_domain_dedication_and_license_v1.0"
            }
        ],
        version="0.2.0",
        views=[
            {
              "name": "graph",
              "title": "VIX - CBOE Volatility Index",
              "specType": "simple",
              "spec": {"type": "line","group": "Date","series": ["VIX Close"]}
            }
        ],
        readme=readme()
    ),
    load(
        load_source='http://www.cboe.com/publish/ScheduledTask/MktData/datahouse/vixcurrent.csv',
        headers=2,
        name='vix-daily'
    ),
    set_type('Date', type='date', format='any'),
    update_resource('vix-daily', **{'title': 'VIX Daily', 'path':'data/vix-daily.csv', 'dpp:streaming': True}),
    validate(),
    dump_to_path(),
)


def flow(parameters, datapackage, resources, stats):
    return finance_vix


if __name__ == '__main__':
    finance_vix.process()
