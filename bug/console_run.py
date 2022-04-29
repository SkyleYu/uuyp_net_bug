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

print("请输入你需要筛选的条件，输入null表示你不需要这个筛选条件")
sort_select = SortWay()

print("请输入你期望这件饰品最少有几个卖家在出租")
res1 = input()
if res1 != "null":
    sort_select.lease_count = int(res1)

print("请输入你期望这件饰品是StatTrak的吗 y/n")
res2 = input()
if res2 == "y" or res2 == "Y":
    sort_select.set_is_StatTrak(True)
elif res2 == "n" or res2 == "N":
    sort_select.set_is_StatTrak(False)

print("请输入你期望这件饰品不超过多少售卖价格呢")
res3 = input()
if res3 != "null":
    sort_select.max_price = float(res3)

print("请输入你期望这件饰品的品质")
print("1：崭新出厂")
print("2：略有磨损")
print("3：久经沙场")
print("4：破损不堪")
print("5：战痕累累")
res4 = input()
if res4 != "null":
    sort_select.set_abrasion_kind(int(res4))

print("请输入你期望这件饰品名字中包含")
res5 = input()
if res5 != "null":
    sort_select.kind = str(res5)

print("请输入你期望这件饰品最小的年短租收益率")
res6 = input()
if res6 != "null":
    sort_select.year_least = float(res6)
# 期许的最小年长租收益
# sort_select.year_long = 0.5
print("请输入你期望这件饰品最小的年长租收益率")
res7 = input()
if res7 != "null":
    sort_select.year_long = float(res7)

# 写文件
with open("./info.txt", "w", encoding="utf-8") as file:
    for item in data_pool.sort_self(sort_select):
        item = str(item).replace('price', "售卖价格").replace('short_unit', "短租价格").replace('long_unit', "长租价格").replace('short_get', "短租年收益").replace('long_get', "长租年收益").replace('lease_count', "出租上架数量")
        print(item)
        file.write(str(item)+"\n")
    file.close()
