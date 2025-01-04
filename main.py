import pandas as pd

import events as ev
import tracking as tr

# Team B @ Team A
dataFrame = pd.read_csv('data/gameAB/2024-10-13.Team.B.@.Team.A.-.Events.csv')

pkDataFrame = ev.get_pk_events_for_game(dataFrame, 1)

away_events = pkDataFrame[0][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]
home_events = pkDataFrame[1][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]

print("Team B @ Team A, Team B PK events")
print(away_events)

print("Team B @ Team A, Team A PK events")
print(home_events)

# Team D @ Team C
dataFrame = pd.read_csv('data/gameCD/2024-11-15.Team.D.@.Team.C.-.Events.csv')

pkDataFrame = ev.get_pk_events_for_game(dataFrame, 0)

away_events = pkDataFrame[0][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]
home_events = pkDataFrame[1][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]

print("Team D @ Team C, Team D PK events")
print(away_events)

print("Team D @ Team C, Team C PK events")
print(home_events)

# Team F @ Team E
dataFrame = pd.read_csv('data/gameEF/2024-11-16.Team.F.@.Team.E.-.Events.csv')

pkDataFrame = ev.get_pk_events_for_game(dataFrame, 0)

away_events = pkDataFrame[0][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]
home_events = pkDataFrame[1][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]

print("Team F @ Team E, Team F PK events")
print(away_events)

print("Team F @ Team E, Team E PK events")
print(home_events)

pkTimes = ev.get_pk_times_for_game(dataFrame)

print('Test')
print(pkTimes)