from os import listdir
from os.path import isfile, join

base_path = '/home/valentinm/Documents/football/datafiles/fixtures_data'

def retrieve_fbref_files(type, league, year):
    """Retrieve files to insert from folder"""
    folders = retrieve_fbref_folders(type, league)
    files = [join(folders[0], f) for f in listdir(folders[0]) if isfile(join(folders[0], f)) and year in f]

    return files

def retrieve_fbref_folders(type, league):
    """Retrieve folders where files are stored"""
    folders = [base_path + '/{0}/{1}/'.format(league, type)]

    return folders

