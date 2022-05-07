# -- coding: utf-8 --
import json
import time

import requests


def fetch_main(page, select_type=None):
    """
    返回post悠悠有品获取饰品信息之后的值
    :param select_type: 对于筛选条件的选择默认是None 代表不开展筛选， 0：刀  1：手枪 2：步枪 3：微冲 4：霰弹枪 5：机枪 6：手套
    :param page:
    :return:
    """
    # 不要改这个这个是获取url的链接
    url = 'https://api.youpin898.com/api/homepage/es/template/GetCsGoPagedList'
    headers = {
        # 这个是请求头，在uu没改的情况下 建议也不要修改
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
        'accept': 'application/json, text/plain, */*',
        'accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-Type': 'application/json;charset=UTF-8'
    }
    # 这个是提交的表单
    data = {
        # 对于刀的指定值 CSGO_Type_Knife
        # "category": "", 指定这个值就会开始筛选
        # 对于手枪的指定值 CSGO_Type_Pistol
        # 对于步枪的指定值 CSGO_Type_Rifle
        # 对于微冲的指定值 CSGO_Type_SMG
        # 对于霰弹枪的指定值 CSGO_Type_Shotgun
        # 对于机枪的指定值 CSGO_Type_Machinegun
        # 对于手套的指定值 Type_Hands
        # 这个应该是csgo游戏的id？我不确定
        "gameId": "730",
        # 这个应该是排序格式？我不确定
        "listSortType": "2",
        # 不清楚这个是什么意思
        "listType": "30",
        # 页码下标（也就是这是在第几页）
        "pageIndex": int(page),
        # 页码单个可以承载的数量
        "pageSize": 924,
        # 不清楚
        "sortType": "0"
    }
    if select_type == 0:
        data["category"] = "CSGO_Type_Knife"
    elif select_type == 1:
        data["category"] = "CSGO_Type_Pistol"
    elif select_type == 2:
        data["category"] = "CSGO_Type_Rifle"
    elif select_type == 3:
        data["category"] = "CSGO_Type_SMG"
    elif select_type == 4:
        data["category"] = "CSGO_Type_Shotgun"
    elif select_type == 5:
        data["category"] = "CSGO_Type_Machinegun"
    elif select_type == 6:
        data["category"] = "Type_Hands"
    elif select_type is None:
        data["pageSize"] = 400  # 尽量不要使用这个接口，有数据缺失的漏洞
    else:
        raise RuntimeError("input error:the args of fetcher: select_type")
    # todo:以上的参数欢迎大家在查看浏览器的开发者网络抓包之后总结补全
    # post参数
    data = json.dumps(data)
    r = requests.post(url, headers=headers, data=data)
    r = r.json()  # 提取json数据
    return r
