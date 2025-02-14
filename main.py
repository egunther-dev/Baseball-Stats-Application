from pybaseball import  playerid_lookup
from pybaseball import  statcast_pitcher
playerid_lookup('kershaw', 'clayton')
kershaw_stats = statcast_pitcher("2017-02-01","2025-01-01",477132)
kershaw_stats.groupby("pitch_type").release_speed.agg("mean")
print(kershaw_stats)