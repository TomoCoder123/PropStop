from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.library.data import *
import pandas as pd


filterd = filter(lambda player: player[player_index_is_active] == True,players)

for filter in filterd:
    print(filter)



