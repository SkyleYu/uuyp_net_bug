# -- coding: utf-8 --
from bug.analysis_data import analysis
from bug.data_pool import DataPool
from bug.fetcher import fetch_main

data_pool = DataPool()
json = {"Code": 0}
page = 1
while True:
    json = fetch_main(page)
    if json["Code"] != 0 or json['Data'] is None:
        break
    page += 1
    analysis(json)
print(data_pool.sort_self())
