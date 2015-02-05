__author__ = 'D'

import numpy
import csv

def my_csv(mode, file_name='my_csv.csv', table=None):
    if mode == 'save':
        with open(file_name, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in table:
                writer.writerow(row)
            print "{0} saved".format(file_name)
    if mode == 'load' or mode == 'open':
        with open(file_name, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            table = [row for row in reader]
        return table

def cluster(data, maxgap):
    data.sort()
    groups = [[data[0]]]
    for x in data[1:]:
        if abs(x - groups[-1][-1]) <= maxgap:
            groups[-1].append(x)
        else:
            groups.append([x])
    return groups


my_price = 79.50
break_even = 55.00


buy_box = 76.48
fulfillment = 'Merchant'
belongs_to_me = False

# price	qt	fulfillment	seller-name	seller-id
offers_table = my_csv('load', 'sample_data.csv')

for row in offers_table:
    print row



