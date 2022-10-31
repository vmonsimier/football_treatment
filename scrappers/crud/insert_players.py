import sys

sys.path.append('/home/valentinm/Documents/football/football_treatment/')

from common import retrieve_fbref_files

def exec(type, league, year):
    files = retrieve_fbref_files(type, league, year)
    files = [f.split('/')[9] for f in files]

    players = []

    for f in files:
        p = f.split('_')[2]
        players.append(p)
    print(players)


exec(sys.argv[1], sys.argv[2], sys.argv[3])