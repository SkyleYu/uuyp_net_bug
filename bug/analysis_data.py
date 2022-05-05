# -- coding: utf-8 --
from bug.data_pool import DataPool


def analysis(json):
    # print (json)
    truely_data_list = json["Data"]
    for data in truely_data_list:
        # 防止价格为0
        if float(data['Price']):
            DataPool.add_data(data["CommodityName"], {
                "price": data['Price'],
                "short_unit": float(data['LeaseUnitPrice']),
                "long_unit": float(data['LongLeaseUnitPrice']),
                "short_get": float(data['LeaseUnitPrice']) * 0.5 * 365 / float(data['Price']),
                "long_get": float(data['LongLeaseUnitPrice']) * 0.73 * 365 / float(data['Price']),
                "lease_count": data["OnLeaseCount"]
            })