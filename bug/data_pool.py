# -- coding: utf-8 --
from bug.sort_select import SortWay


class DataPool(object):
    __cache = {}

    @staticmethod
    def add_data(name, data):
        DataPool.__cache[name] = data

    @staticmethod
    def print_cahce():
        """
        直接打印cache池中的参数
        :return:
        """
        print(DataPool.__cache)

    @staticmethod
    def sort_self(sort_way: SortWay = None):
        """
        对本池进行排序，注意这里返回的不是一个dict了，而是一个key+value的元组的list
        :return:
        """
        # DataPool.print_cahce()
        all_item = sorted(DataPool.__cache, key=lambda a:DataPool.__cache[a]["short_get"], reverse=True)
        pass_list = []
        for item in all_item:
            pass_list.append((item, DataPool.__cache[item]))
        if sort_way:
            return sort_way.get_pass(pass_list)
        else:
            return pass_list
