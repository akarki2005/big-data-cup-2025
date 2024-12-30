import pandas as pd

# create dataFrame from csv
dataFrame = pd.read_csv('data/gameAB/2024-10-13.Team.B.@.Team.A.-.Events.csv')

# Note: I'm currently only considering 5 on 4 powerplays, but i'll probably ensure support for 5 on 3 and 4 on 3 as well (5 on 3 will probably be seperate from the others)

# HOME PENALTY KILL
 
# Period 1 (pk on right side)

p1dfh = dataFrame[(dataFrame['Period'].isin([1])) & (dataFrame['Home_Team_Skaters'] == 4) & (dataFrame['Away_Team_Skaters'] == 5) & (dataFrame['X_Coordinate'] >= 25)]

# Period 2 (pk on left side)

p2dfh = dataFrame[(dataFrame['Period'].isin([2])) & (dataFrame['Home_Team_Skaters'] == 4) & (dataFrame['Away_Team_Skaters'] == 5) & (dataFrame['X_Coordinate'] <= -25)]

# Period 3 (pk on right side)

p3dfh = dataFrame[(dataFrame['Period'].isin([3])) & (dataFrame['Home_Team_Skaters'] == 4) & (dataFrame['Away_Team_Skaters'] == 5) & (dataFrame['X_Coordinate'] >= 25)]

# join together

home_pk = pd.concat([p1dfh, p2dfh, p3dfh], sort = True)
print(home_pk)

# AWAY PENALTY KILL
 
# Period 1 (pk on left side)

p1dfa = dataFrame[(dataFrame['Period'].isin([1])) & (dataFrame['Home_Team_Skaters'] == 5) & (dataFrame['Away_Team_Skaters'] == 4) & (dataFrame['X_Coordinate'] <= -25)]

# Period 2 (pk on right side)

p2dfa = dataFrame[(dataFrame['Period'].isin([2])) & (dataFrame['Home_Team_Skaters'] == 5) & (dataFrame['Away_Team_Skaters'] == 4) & (dataFrame['X_Coordinate'] >= 25)]

# Period 3 (pk on left side)

p3dfa = dataFrame[(dataFrame['Period'].isin([3])) & (dataFrame['Home_Team_Skaters'] == 5) & (dataFrame['Away_Team_Skaters'] == 4) & (dataFrame['X_Coordinate'] <= -25)]

# join together

away_pk = pd.concat([p1dfa, p2dfa, p3dfa], sort = True)
print(away_pk)