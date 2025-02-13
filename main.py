from pybaseball import batting_stats 
from tabulate import tabulate 

# Fetch MLB batting stats for a specific year
year = 2023
stats = batting_stats(year)

# Convert stats DataFrame to a list of dictionaries for easier processing
stats_list = stats.to_dict(orient="records")

# Define the player to search for
player_name = "Aaron Judge"

# Search for player
player_stats = next((player for player in stats_list if player["Name"] == player_name), None)

if player_stats:
    # Define the columns to display
    columns = [
        "Name", "Team", "G", "AB", "R", "H", "HR", "SB", "RBI", "BB", "SO", "SB", "CS", "AVG", "OBP", "SLG", "OPS"
    ]

    # Extract selected stats for display
    row = [player_stats[col] for col in columns]

    # Print table in a structured format
    print(tabulate([row], headers=columns, tablefmt="fancy_grid"))

else:
    print(f"Player {player_name} not found in {year} stats.")
