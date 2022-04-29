# -- coding: utf-8 --
class DataPool(object):
    __cache = {}

    @staticmethod
    def add_data(name, data):
        DataPool.__cache[name] = data

    @staticmethod
    def print_cahce():
        print(DataPool.__cache)

    @staticmethod
    def sort_self():
        # DataPool.print_cahce()
        all_item = sorted(DataPool.__cache, key=lambda a:DataPool.__cache[a]["short_get"], reverse=True)
        for item in all_item:
            if "StatTrak" in item:
                continue
            if DataPool.__cache[item]["lease_count"] < 10:
                continue
            print(item, DataPool.__cache[item])