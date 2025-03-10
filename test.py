from pybaseball import playerid_lookup, pitching_stats, batting_stats
from pybaseball import statcast_pitcher
import pandas as pd
def start():

    while True:
        s = input("Choose an option (Enter only the number, anything else will re-prompt you):\n1. Pitching Stats\n2. Hitting Stats\n3. Standings\n")
        if s.strip() == "1": 
            get_pitcher_stats()
        elif s.strip() == "2":
            get_hitting_stats()
        #elif s.strip() == "3":
            #league_standings()
        else:
            continue
        break

def get_pitcher_stats():
    pitcher_last = input("Enter pitchers last name: ").strip()
    pitcher_first = input("Enter pitchers first name: ").strip()

    player_info = playerid_lookup(pitcher_last, pitcher_first)

    if player_info.empty:
        print("Player not found")
        return
    print(player_info)

    player_id = player_info.iloc[0]['key_fangraphs'] # Credit: ChatGPT, used GPT to debug it giving no stats found, told me I needed to get fangraphs, not MLBAM 
    print(f"Fangraphs ID for {pitcher_first} {pitcher_last}: {player_id}")


    start_season = input("Enter Start Season: ")
    end_season = input("Enter End Season: ")
    print("Processing...")
    stats = pitching_stats(start_season, end_season)


    if player_id not in stats["IDfg"].values:
        print(f"No stats found for {pitcher_first} {pitcher_last} from {start_season} to {end_season}.")
        return
    
    pitcher_stats = stats[stats['IDfg'] == player_id]
    pitcher_stats = pitcher_stats.sort_values(by="Season")

    selected_columns = ['Name', 'Team', 'Season', 'W', 'L', 'ERA', 'WAR', 'SO', 'WHIP']
    print("Pitching Stats")
    print(pitcher_stats[selected_columns])

def get_hitting_stats():
    data = batting_stats(2023)
    pd.set_option('display.max_rows',None)
    data = data.sort_index()

    print(data)

start()
