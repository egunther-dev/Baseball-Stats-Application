from pybaseball import playerid_lookup, pitching_stats
from pybaseball import statcast_pitcher

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



get_pitcher_stats()