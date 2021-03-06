import enum


class Stats(enum.Enum):
    ast = 0
    blk = 1
    dreb = 2
    fg3_pct = 3
    fg3a = 4
    fg3m = 5
    fg_pct = 6
    fga = 7
    fgm = 8
    ft_pct = 9
    fta = 10
    ftm = 11
    games_played = 12
    seconds = 13
    oreb = 14
    pf = 15
    player_id = 16
    pts = 17
    reb = 18
    season = 19
    stl = 20
    turnover = 21


class Games(enum.Enum):
    home_team_id = 0
    home_team_score = 1
    season = 2
    postseason = 3
    visitor_team_id = 4
    visitor_team_score = 5
