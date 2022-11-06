import json
import os

def save(path, fileName, player_pos, player_health, deaths, player_weapon):
    print('Player data =: ' + data)
    data = (player_pos, player_health, player_weapon, deaths, INV_TBL)
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
json_path = 'data/saves'
json_fileName = 'save0'

json_data = {}
json_data['test'] = 'test2'
json_data['foo'] = 'bar'


#Reading
#Path to data
CWD = os.getcwd()
INVENTORY = '%s/%s' % (CWD, 'data/inventory.json')
ITEM_LOOKUP = '%s/%s' % (CWD, 'data/items_lookup.json')


#dictior
INV_TBL = {}
ITEM_DICT = {}

# open and read shit
try:
    with open(ITEM_LOOKUP) as itemlist_file:
        ITEM_DICT = json.load(itemlist_file)
    with open(INVENTORY) as inv_file:
        INV_TBL = json.load(inv_file)
except IOError as e:
    print(e)
    print('IOError: Unable to open file!')
    exit(1)

print(INV_TBL)