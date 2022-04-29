# -- coding: utf-8 --
from bug.analysis_data import analysis
from bug.data_pool import DataPool
from bug.fetcher import fetch_main
from bug.sort_select import SortWay

data_pool = DataPool()

page = 1
while True:
    json = fetch_main(page)
    if json["Code"] != 0 or json['Data'] is None:
        break
    page += 1
    analysis(json)

sort_select = SortWay()
# 最小出租数量为10
sort_select.lease_count = 10
# 不是计数器物品
sort_select.set_is_StatTrak(False)
# 售卖价格小于799
# sort_select.max_price = 799
# 品质为久经沙场
# sort_select.set_abrasion_kind(3)
# 名称中含有大马士革钢
# sort_select.kind = "大马士革钢"
# 期许的最小年短租收益
sort_select.year_least = 0.35
# 期许的最小年长租收益
# sort_select.year_long = 0.5

# 写文件
with open("./info.txt", "w", encoding="utf-8") as file:
    for item in data_pool.sort_self(sort_select):
        print (item)
        item = str(item).replace('price', "售卖价格").replace('short_unit', "短租价格").replace('long_unit', "长租价格").replace('short_get', "短租年收益").replace('long_get', "长租年收益").replace('lease_count', "出租上架数量")
        file.write(str(item)+"\n")
    file.close()
