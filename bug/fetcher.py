# -- coding: utf-8 --
import json
import time

import requests


def fetch_main(page, data=None):
    """
    返回post悠悠有品获取饰品信息之后的值
    :param page:
    :param data: 默认为None，详情表单参数参照下文data的值，你可以指定发送的表单，当然建立在你对其完全了解的情况下
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
        # 对于刀的指定值
        "category": "CSGO_Type_Knife",
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
    # todo:以上的参数欢迎大家在查看浏览器的开发者网络抓包之后总结补全
    # post参数
    data = json.dumps(data)
    r = requests.post(url, headers=headers, data=data)
    r = r.json()  # 提取json数据
    return r

