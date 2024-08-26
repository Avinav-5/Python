# Sample data of past ODI matches
match_data = [
    {"date": "2023-01-01", "opponent": "Australia", "venue": "Mumbai", "result": "Win", "players": {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"}},
    {"date": "2023-01-10", "opponent": "England", "venue": "Lord's", "result": "Loss", "players": {"Virat Kohli", "Rohit Sharma"}},
    {"date": "2023-02-15", "opponent": "Australia", "venue": "Sydney", "result": "Loss", "players": {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"}},
    {"date": "2023-03-01", "opponent": "South Africa", "venue": "Cape Town", "result": "Win", "players": {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"}},
    {"date": "2023-03-10", "opponent": "England", "venue": "Mumbai", "result": "Win", "players": {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"}},
]

# Calculate win/loss ratio for home and away matches
performance = {"Home": {"Win": 0, "Loss": 0}, "Away": {"Win": 0, "Loss": 0}}

for match in match_data:
    venue = "Home" if match["venue"] == "Mumbai" else "Away"
    if match["result"] == "Win":
        performance[venue]["Win"] += 1
    else:
        performance[venue]["Loss"] += 1

print("Home/Away Performance:", performance)

# Analyze the impact of key players
key_players = {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"}
key_player_wins = 0
total_key_player_matches = 0

for match in match_data:
    if key_players.issubset(match["players"]):
        total_key_player_matches += 1
        if match["result"] == "Win":
            key_player_wins += 1

if total_key_player_matches > 0:
    key_player_win_ratio = key_player_wins / total_key_player_matches
else:
    key_player_win_ratio = 0

print(f"Key Player Win Ratio: {key_player_win_ratio:.2f}")

# Analyze performance against specific opponents
opponent_performance = {}

for match in match_data:
    opponent = match["opponent"]
    if opponent not in opponent_performance:
        opponent_performance[opponent] = {"Win": 0, "Loss": 0}
    if match["result"] == "Win":
        opponent_performance[opponent]["Win"] += 1
    else:
        opponent_performance[opponent]["Loss"] += 1

print("Performance by Opponent:", opponent_performance)

# Function to predict match outcome based on opponent, venue, and players
def predict_outcome(opponent, venue, players):
    # Check opponent performance
    if opponent_performance.get(opponent, {"Win": 0, "Loss": 0})["Win"] > opponent_performance[opponent]["Loss"]:
        # Check venue performance
        if "Home" in venue and performance["Home"]["Win"] > performance["Home"]["Loss"]:
            # Check key player availability
            if key_players.issubset(players):
                return "Predicted Result: Win"
    return "Predicted Result: Loss"

m=predict_outcome("South Africa","Cape Town",{"Virat kohli","Rohit sharma","Jasprit Bumrah"})
print(m)

# # Test cases for prediction
# test_match_1 = {"opponent": "Australia", "venue": "Mumbai", "players": {"Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"}}
# test_match_2 = {"opponent": "England", "venue": "Lord's", "players": {"Virat Kohli", "Rohit Sharma"}}

# print(predict_outcome(test_match_1["opponent"], test_match_1["venue"], test_match_1["players"]))
# print(predict_outcome(test_match_2["opponent"], test_match_2["venue"], test_match_2["players"]))
