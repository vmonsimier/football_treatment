from operator import index
import sys
from os import listdir
from os.path import isfile, join
import csv
import itertools

sys.path.append('/home/valentinm/Documents/football/football_treatment/')

import database
from fbref_to_db_columns_db import get_map_columns

base_path = '/home/valentinm/Documents/football/datafiles/fixtures_data'

def exec(type, league, year):
    files = retrieve_files(type, league, year)
    print(len(files))

    batch_ins = []

    for file in files:
        csv_data = get_csv_data(file)
        format_d = format_data(type, csv_data)
        batch_ins.append(format_d)
        batch_ins = list(itertools.chain(*batch_ins))

    # split and insert by 1000 rows
    #conn = database.connect()

def retrieve_files(type, league, year):
    """Retrieve files to insert from folder"""
    folders = retrieve_folders(type, league)
    files = [join(folders[0], f) for f in listdir(folders[0]) if isfile(join(folders[0], f)) and year in f]

    return files

def retrieve_folders(type, league):
    """Retrieve folders where files are stored"""
    folders = [base_path + '/{0}/{1}/'.format(league, type)]

    return folders

def get_csv_data(filename):
    """Read csv file and get data"""
    data = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            if len(row) > 0 and row[0].strip() != '' and 'données SR' not in row[0]:
                data.append(row) 

    return data

def format_data(type, data):
    """Format data before insert"""
    columns = data[0]
    data.pop(0)

    map_columns = get_map_columns(type)
    index_val = get_index_val(columns, map_columns)

    formated = []

    for item in data:
        item_f = []
        #Retrieve or insert and get fixture_id
        #Retrieve player_id
        for i in index_val:
            item_f.append(item[i])
        formated.append(item_f)

    return formated
        
def get_index_val(cols, map_cols):
    values = list(map_cols.values())
    index = []
    for val in values:
        if val[1] == 0:
            i = cols.index(val[0])
            index.append(i)
        else:
            a = 0
            for j in range(0, val[1] + 1):
                i = cols.index(val[0], a + 1)
                a = i
            index.append(a)
            
    return index


exec(sys.argv[1], sys.argv[2], sys.argv[3])