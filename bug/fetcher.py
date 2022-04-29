# -- coding: utf-8 --
import json
import time

import requests


def fetch_main(page):
    url = 'https://api.youpin898.com/api/homepage/es/template/GetCsGoPagedList'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
        'accept': 'application/json, text/plain, */*',
        'accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        "category": "CSGO_Type_Knife",
        "gameId": "730",
        "listSortType": "2",
        "listType": "30",
        "pageIndex": int(page),
        "pageSize": 924,
        "sortType": "0"
    }
    # post参数
    data = json.dumps(data)
    r = requests.post(url, headers=headers, data=data)
    r = r.json()  # 提取json数据
    return r

