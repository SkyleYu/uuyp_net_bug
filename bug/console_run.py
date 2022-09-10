# -- coding: utf-8 --
from bug import detail_fetcher
from bug.analysis_data import analysis
from bug.data_pool import DataPool
from bug.fetcher import fetch_main
from bug.sort_select import SortWay

data_pool = DataPool()

print("请输入你需要查找的种类：")
print("8：不限")
print("0: 只有刀")
print("1: 只有手枪")
print("2: 只有步枪（包括狙击枪）")
print("3: 只有冲锋枪")
print("4: 只有散弹枪")
print("5: 只有机枪")
print("6: 只有手套")
print("7: 只有任何类型的枪")
print("可以设置多个选择条件，如输入06，则代表可以同时指定枪与刀")
res0 = input()

print("正在获取网络数据中，请稍后...")
if "7" in res0:
    res0 = res0.replace("7", "12345")
if "8" in res0:
    res0 = res0.replace("8", "0123456")
if res0:
    for key in res0:
        page = 1
        while True:
            json = fetch_main(page, select_type=int(key))
            if json["Code"] != 0 or json['Data'] is None:
                break
            page += 1
            analysis(json)
else:
    page = 1
    while True:
        json = fetch_main(page, select_type=None)
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

print("请输入你期望这件饰品是StatTrak的吗 y/n/null（null代表两者都可）")
res2 = input()
if res2 == "y" or res2 == "Y":
    sort_select.set_is_StatTrak(True)
elif res2 == "n" or res2 == "N":
    sort_select.set_is_StatTrak(False)

print("请输入你期望这件饰品是纪念品的吗 y/n/null（null代表两者都可）")
G_res = input()
if G_res == "y" or G_res == "Y":
    sort_select.set_is_Guardar(True)
elif G_res == "n" or G_res == "N":
    sort_select.set_is_Guardar(False)

print("请输入你期望这件饰品不超过多少售卖价格呢")
res3 = input()
if res3 != "null":
    sort_select.max_price = float(res3)

print("请输入你期望这件饰品最低需要多少售卖价格呢")
res8 = input()
if res8 != "null":
    sort_select.min_price = float(res8)

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

print("请输入你期望这件饰品名字中不包含")
unkind_res = input()
if unkind_res != "null":
    sort_select.unkind = str(unkind_res)

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

print("是否查看过往交易信息？1：仅查看租赁信息 2：仅查看售卖信息 3：查看租赁与售卖信息 null：不查看")
res8 = input()


def detail_api_weak_up(yn_flag, target_file, target_item):
    if yn_flag != "null":
        print("正在获取过往交易信息，请稍后...")
        if yn_flag == "1" or yn_flag == "3":
            print('租赁信息: \n')
            target_file.write('租赁信息: \n')
            ret_json = detail_fetcher.detail_ret_fetcher(target_item[1]['id'])
            ret_str_list = detail_fetcher.ret_detail_analysis(ret_json)
            for single_ret_str in ret_str_list:
                print(single_ret_str + '\n')
                target_file.write(single_ret_str + '\n')
        if yn_flag == "2" or yn_flag == "3":
            print('售卖信息: \n')
            target_file.write('售卖信息: \n')
            sale_json = detail_fetcher.detail_sale_fetcher(target_item[1]['id'])
            sale_str_list = detail_fetcher.sale_detail_analysis(sale_json)
            for single_sale_str in sale_str_list:
                print(single_sale_str + '\n')
                target_file.write(single_sale_str + '\n')


# 写文件
with open("./info.txt", "w", encoding="utf-8") as file:
    for item in data_pool.sort_self(sort_select):
        item_str = str(item).replace('price', "售卖价格").replace('short_unit', "短租价格").replace('long_unit', "长租价格").replace(
            'short_get', "短租年收益").replace('long_get', "长租年收益").replace('lease_count', "出租上架数量")
        print(item_str)
        file.write(str(item_str) + "\n")
        detail_api_weak_up(res8, file, item)
    file.close()
input('按任意键退出')
