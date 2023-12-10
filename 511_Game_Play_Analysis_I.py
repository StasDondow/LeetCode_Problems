# https://leetcode.com/problems/game-play-analysis-i/

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    res = activity[["player_id", "event_date"]]
    res = res.rename(columns={"event_date": "first_login"})

    min_date_indices = res.groupby("player_id")["first_login"].idxmin()

    return res.loc[min_date_indices]
