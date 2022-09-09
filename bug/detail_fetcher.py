import json

import requests

headers = {
    # 这个是请求头，在uu没改的情况下 建议也不要修改
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'accept': 'application/json, text/plain, */*',
    'accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-Type': 'application/json;charset=UTF-8'
}


def detail_ret_fetcher(item_id):
    """
    请求饰品的详细信息
    :param item_id:饰品的id，在返回值众寻找
    :return:
    """
    # 出租信息查询url
    ret_url = "https://api.youpin898.com/api/trade/Order/GetTopLeaseOutOrderList?TemplateId={}".format(item_id)
    ret_res = requests.get(ret_url, headers=headers)
    return ret_res.json()


def detail_sale_fetcher(item_id):
    """
    请求饰品的详细信息
    :param item_id:饰品的id，在返回值众寻找
    :return:
    """
    # 售卖信息url
    sale_url = "https://api.youpin898.com/api/trade/Order/GetTopOfferOrderList?TemplateId={}".format(item_id)
    sale_res = requests.get(sale_url, headers=headers)
    return sale_res.json()


def ret_detail_analysis(data):
    """
    分析出租信息
    :param data: 出租信息
    :return:
    """
    data = data["Data"]
    return_list = []
    for each_data in data:
        detail_str = "出租类型:{}, 单日价格:{}, 租赁日期:{}, 租赁押金:{}, 租出日期:{} ".format("长租" if each_data["Type"] == 1 else "短租", each_data["LeaseUnitPrice"], each_data["LeaseDays"], each_data["LeaseDeposit"], each_data["DateTime"])
        return_list.append(detail_str)
    return return_list


def sale_detail_analysis(data):
    """
    分析售卖信息
    :param data: 售卖信息
    :return:
    """
    data = data["Data"]
    return_list = []
    for each_data in data:
        detail_str = "出售价格:{}, 出售日期:{}, 具体时间:{} ".format(each_data["Price"], each_data["DateTime"], each_data["CompleteTime"])
        return_list.append(detail_str)
    return return_list

