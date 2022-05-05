# -- coding: utf-8 --
class SortWay(object):
    def __init__(self):
        # 是否为计数器的筛选
        self.is_StatTrak = None
        # 品质的筛选
        self.abrasion = None
        # 以下的属性因为没有什么特殊的直接在外部访问就好
        # 饰品名称的筛选
        self.kind = None
        # 最大价格的筛选（大于此值会被跳过）
        self.max_price = None
        # 最小价格的筛选（小于此值会被跳过）
        self.min_price = None
        # 期许的短租收益的筛选（小于此值会被跳过）
        self.year_least = None
        # 期许的长租收益的筛选（大于此值会被跳过）
        self.year_long = None
        # 最小售卖数量,用于排除只有几个饰品在市，恶意抬价的现象
        self.lease_count = None

    def set_is_StatTrak(self, value: bool):
        """
        设置是否是计数器
        :param value:
        :return:
        """
        self.is_StatTrak = value

    def set_abrasion_kind(self, ab_index: int):
        """
        设置品质
        1：崭新出厂
        2：略有磨损
        3：久经沙场
        4：破损不堪
        5：战痕累累
        :param ab_index:
        :return:
        """
        if ab_index == 1:
            self.abrasion = "崭新出厂"
        elif ab_index == 2:
            self.abrasion = "略有磨损"
        elif ab_index == 3:
            self.abrasion = "久经沙场"
        elif ab_index == 4:
            self.abrasion = "破损不堪"
        elif ab_index == 4:
            self.abrasion = "战痕累累"

    def get_pass(self, item_list):
        """
        接受一个[(饰品名称, {饰品json被analysis函数解析之后的字典}]的列表
        :param item_list:
        :return:
        """
        return_list = []
        for item in item_list:
            if self.is_StatTrak is not None:
                if self.is_StatTrak:
                    if "StatTrak" not in item[0]:
                        continue
                else:
                    if "StatTrak" in item[0]:
                        continue
            if self.abrasion is not None:
                if self.abrasion not in item[0]:
                    continue
            if self.kind is not None:
                if self.kind not in item[0]:
                    continue
            if self.max_price is not None:
                if float(item[1]["price"]) >= self.max_price:
                    continue
            if self.min_price is not None:
                if float(item[1]["price"]) < self.min_price:
                    continue
            if self.year_least is not None:
                if float(item[1]["short_get"]) < self.year_least:
                    continue
            if self.year_long is not None:
                if float(item[1]["long_get"]) < self.year_long:
                    continue
            if self.lease_count is not None:
                if item[1]["lease_count"] < self.lease_count:
                    continue
            return_list.append(item)
        return return_list
