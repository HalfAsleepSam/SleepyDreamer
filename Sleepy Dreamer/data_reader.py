import json
import time
import os

#Path to data
CWD = os.getcwd()
INVENTORY = '%s/%s' % (CWD, 'data/inventory.json')
ITEM_LOOKUP = '%s/%s' % (CWD, 'data/items_lookup.json')


#dictior
REQUEST = {}

# open and read shit
try:
    with open(INVENTORY) as data_file:
        REQUEST = json.load(data_file)
except IOError as e:
    print(e)
    print('IOError: Unable to open file!')
    exit(1)


print(REQUEST)