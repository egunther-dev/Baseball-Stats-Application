from pybaseball import playerid_lookup, pitching_stats
from pybaseball import statcast_pitcher

def get_pitcher_stats():
    pitcher_last = input("Enter pitchers last name: ").strip()
    pitcher_first = input("Enter pitchers first name: ").strip()

    player_info = playerid_lookup(pitcher_last, pitcher_first)

    if player_info.empty:
        print("Player not found!")
        return
    print(player_info)

    player_id = player_info.iloc[0]['key_mlbam']
    print(f"MLBAM ID for {pitcher_first} {pitcher_last}: {player_id}")


    start_season = input("Enter Start Season: ")
    end_season = input("Enter End Season: ")

    stats = pitching_stats(start_season, end_season)

    pitcher_stats = stats[stats['IDfg'] == player_id]
    if pitcher_stats.empty:
        print(f"No stats found for {pitcher_first} {pitcher_last} in {start_season}-{end_season}")
        return

    selected_columns = ['Name', 'Team', 'Season', 'W', 'L', 'ERA', 'WAR', 'SO', 'WHIP']
    print(pitcher_stats[selected_columns])



if __name__ == "__main__":
    get_pitcher_stats()