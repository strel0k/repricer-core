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
    if mode == 'load':
        with open(file_name, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            table = [table.append(row) for row in reader]
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



asin = 'B003XNFROU'
msku = 'KITRA-1943'


fba_data = {msku: {'your-price': 10.00}}
dp_data = {msku: {'break_even': }}
il_data = {msku: {'cost': }}


buy_box = {asin: {'New': {'landed_price': 10.00}}}
belongs_to_requester = True

offer_price =


# [landed_price, fulfillment, seller_id]



# if I DONT hold the buy box...
reprice_trigger = {'status': False, 'reason': None}
if not belongs_to_requester:
    # am I in the bb rotation?
    landed_price = buy_box[asin]['New']['landed_price']
    your_price = fba_data[msku]['your-price'] # using 24 delayed data #TODO: fix this
    #TODO: this part needs improvement for accuracy
    if your_price > landed_price * 0.995 and your_price < landed_price * 1.005:
        reprice_trigger['status'] = False
    else:
        reprice_trigger['status'] = True
        reprice_trigger['reason'] = 'not in bb rotation'
    # if amazon holds buy box I am defiantly not in the rotation
    for i in lowest_offers:
        if i[0] == landed_price:
            if i[2] == 'Amazon.com':
                reprice_trigger['status'] = True
                reprice_trigger['reason'] = 'amazon in bb'
    #TODO: is my rotation % sufficient?
    # save bb status for rotation % calculation
    # for this we will have to record my bb status each time script is run, and get a % from that


# if a reprice is triggered
if reprice_trigger['status']:
    # get a list of prime seller prices
    prime_seller_prices = []
    for i in lowest_offers:
        if i[1] == 'Amazon':
            prime_seller_prices.append(i[0])
    # create cluster with max gap of $0.05
    price_cluster = cluster(prime_seller_prices, 0.10)
    # set target price to median of lowest price cluster
    if type(price_cluster[0]) is list:
        target_price = numpy.median(price_cluster[0])
    # if there is no clustering
    else:
        target_price = numpy.median(price_cluster)

    if reprice_trigger['reason'] == 'amazon in bb':
        target_price = round(target_price * 0.997, 2)
    print price_cluster
    print price_cluster[0]

    # get break even price
    break_even = dp_data[msku]['break_even']
    your_price = fba_data[msku]['your-price'] # using 24 delayed data #TODO: fix this
    if target_price > break_even:
        print "Set price to target price."
        print "Result action: {0} > {1}".format(your_price, target_price)
    else:
        print "Target price below break even price, ask for exception."
        buy_cost = il_data[msku]['cost']
        print "Your Price: {3}  Target: {2}  Buy cost: {0}  Break even: {1}".format(buy_cost, break_even,
                                                                                    target_price, your_price)