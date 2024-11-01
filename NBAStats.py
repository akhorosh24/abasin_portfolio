"""
This program pulls NBA Stats from NBA.com

"""

import pandas as pd
import requests

NBA_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2014-15&SeasonType=Regular%20Season&StatCategory=PTS'
data = requests.get(url=NBA_url).json()

sourceCols = r['resultSet']['headers']

dataCols = ['Year', 'Season Type'] + sourceCols
dataTable = pd.DataFrame(columns = dataCols)

SEASON = ['2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
SEASON_TYPE = ['Regular%20Season', 'Playoffs']

for i in SEASON:
    for j in SEASON_TYPE:
        NBA_url_10 = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=' + i + '&SeasonType=' + j + '&StatCategory=PTS'
        
        scrape = requests.get(url=NBA_url_10).json()
        
        df1 = pd.DataFrame(scrape['resultSet']['rowSet'], columns = sourceCols)
        df2 = pd.DataFrame({'Year':[i for k in range(len(df1))], 
                         'Season Type':[j for k in range(len(df1))]})
        df3 = pd.concat([df2, df1], axis = 1)
        
        dataTable = pd.concat([dataTable, df3], axis = 0)

dataTable.to_excel('NBA_Stats.xlsx', index = False)
