# 设置一个列表为11个None
from bug import detail_fetcher
from bug.analysis_data import analysis
from bug.data_pool import DataPool
from bug.fetcher import fetch_main
from bug.sort_select import SortWay

res = [''] * 12
cnt = 0
with open("./config.txt", encoding='utf-8') as config:
    for single_line in config.readlines():
        if "$(请勿删除此标识符)" in single_line:
            line = single_line[11:]
            # 去掉\n
            if line.endswith('\n'):
                line = line[:-1]
            # 防呆检测'：'
            if line.startswith(':') or line.startswith('：'):
                line = line[1:]
            line = 'res[' + str(cnt) + ']=\'' + line + '\''
            exec(line)
            cnt += 1
for singe_res_index in range(res.__len__()):
    # 去除single_res中的空格
    res[singe_res_index] = res[singe_res_index].replace(' ', '')

data_pool = DataPool()
print("正在获取网络数据中，请稍后...")
if "7" in res[0]:
    res[0] = res[0].replace("7", "12345")
if "8" in res[0]:
    res0 = res[0].replace("8", "0123456")
if res[0]:
    for key in res[0]:
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

sort_select = SortWay()

if res[1] != "null":
    sort_select.lease_count = int(res[1])

if res[2] == "y" or res[2] == "Y":
    sort_select.set_is_StatTrak(True)
elif res[2] == "n" or res[2] == "N":
    sort_select.set_is_StatTrak(False)

if res[3] == "y" or res[3] == "Y":
    sort_select.set_is_Guardar(True)
elif res[3] == "n" or res[3] == "N":
    sort_select.set_is_Guardar(False)

if res[4] != "null":
    sort_select.max_price = float(res[4])

if res[5] != "null":
    sort_select.min_price = float(res[5])

if res[6] != "null":
    sort_select.set_abrasion_kind(int(res[6]))

if res[7] != "null":
    sort_select.kind = str(res[7])

if res[8] != "null":
    sort_select.unkind = str(res[8])

if res[9] != "null":
    sort_select.year_least = float(res[9])
# 期许的最小年长租收益
# sort_select.year_long = 0.5
if res[10] != "null":
    sort_select.year_long = float(res[10])


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
        detail_api_weak_up(res[11], file, item)
    file.close()
