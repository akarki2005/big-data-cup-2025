import pandas as pd

## FUNCTIONS

def get_pk_events_for_game(data: pd.DataFrame, right_side_team: int) -> tuple[pd.DataFrame, pd.DataFrame]: 
    # data: the event data for the game
    # right_side_team: the team whose defending zone is on the right for periods 1 and 3 (0 for away team, 1 for home team)

    if right_side_team: # home team on the right for p1 and p3
        # get away penalty kill event data
        p1a = get_pk_events_for_period(data, 1, 0, 0)
        p2a = get_pk_events_for_period(data, 2, 0, 1)
        p3a = get_pk_events_for_period(data, 3, 0, 0)
        # get home penalty kill event data
        p1h = get_pk_events_for_period(data, 1, 1, 1)
        p2h = get_pk_events_for_period(data, 2, 1, 0)
        p3h = get_pk_events_for_period(data, 3, 1, 1)
    else: # away team on the right for p1 and p3
        # get away penalty kill event data
        p1a = get_pk_events_for_period(data, 1, 0, 1)
        p2a = get_pk_events_for_period(data, 2, 0, 0)
        p3a = get_pk_events_for_period(data, 3, 0, 1)
        # get home penalty kill event data
        p1h = get_pk_events_for_period(data, 1, 1, 0)
        p2h = get_pk_events_for_period(data, 2, 1, 1)
        p3h = get_pk_events_for_period(data, 3, 1, 0)


    return (pd.concat([p1a, p2a, p3a], sort=True), pd.concat([p1h, p2h, p3h], sort=True))


def get_pk_events_for_period(data: pd.DataFrame, period: int, team: int, side: int) -> pd.DataFrame:
    # data: the event data for the game
    # period: the period to get pk events for 
    # team: the team to get pk events for (0 for away, 1 for home)
    # side: the side that they are defending (0 for left, 1 for right)
    if team: # home team
        if side: # right side
            return data[(data['Period'] == period) & (data['Home_Team_Skaters'] < data['Away_Team_Skaters']) & (data['X_Coordinate'] > 25)]
        else: # left side
            return data[(data['Period'] == period) & (data['Home_Team_Skaters'] < data['Away_Team_Skaters']) & (data['X_Coordinate'] < -25)]
    else: # away team
        if side: # right side
            return data[(data['Period'] == period) & (data['Home_Team_Skaters'] > data['Away_Team_Skaters']) & (data['X_Coordinate'] > 25)]
        else: # left side
            return data[(data['Period'] == period) & (data['Home_Team_Skaters'] > data['Away_Team_Skaters']) & (data['X_Coordinate'] < -25)]


# Team B @ Team A
dataFrame = pd.read_csv('data/gameAB/2024-10-13.Team.B.@.Team.A.-.Events.csv')

pkDataFrame = get_pk_events_for_game(dataFrame, 1)

away_events = pkDataFrame[0][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]
home_events = pkDataFrame[1][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]

print("Team B @ Team A, Team B PK events")
print(away_events)

print("Team B @ Team A, Team A PK events")
print(home_events)

# Team D @ Team C
dataFrame = pd.read_csv('data/gameCD/2024-11-15.Team.D.@.Team.C.-.Events.csv')

pkDataFrame = get_pk_events_for_game(dataFrame, 0)

away_events = pkDataFrame[0][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]
home_events = pkDataFrame[1][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]

print("Team D @ Team C, Team D PK events")
print(away_events)

print("Team D @ Team C, Team C PK events")
print(home_events)

# Team F @ Team E
dataFrame = pd.read_csv('data/gameEF/2024-11-16.Team.F.@.Team.E.-.Events.csv')

pkDataFrame = get_pk_events_for_game(dataFrame, 0)

away_events = pkDataFrame[0][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]
home_events = pkDataFrame[1][['Period', 'Clock', 'Away_Team_Goals', 'Home_Team_Goals', 'Event', 'Team']]

print("Team F @ Team E, Team F PK events")
print(away_events)

print("Team F @ Team E, Team E PK events")
print(home_events)