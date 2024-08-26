# Function to load data from CSV file
def load(file):
    matches = []
    with open(file, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        
        for line in lines[1:]:
            parts = line.strip().split(',')
            date = parts[0]
            opponent = parts[1]
            venue = parts[2]
            result = parts[3]
            runs_scored = int(parts[4])
            wickets_taken = int(parts[5])
            player_of_match = parts[6]
            
            matches.append({
                "date": date,
                "opponent": opponent,
                "venue": venue,
                "result": result,
                "runs_scored": runs_scored,
                "wickets_taken": wickets_taken,
                "player_of_match": player_of_match
            })
    return matches

# Function to analyze overall match data
def analyze_matches(matches):
    total_matches = len(matches)
    wins = 0
    losses = 0
    ties = 0
    total_runs = 0
    total_wickets = 0
    player_of_match_count = {}

    for match in matches:
        if match["result"] == "Win":
            wins += 1
        elif match["result"] == "Loss":
            losses += 1
        elif match["result"] == "Tied":
            ties += 1

        total_runs += match["runs_scored"]
        total_wickets += match["wickets_taken"]

        player = match["player_of_match"]
        if player in player_of_match_count:
            player_of_match_count[player] += 1
        else:
            player_of_match_count[player] = 1

    win_percentage = (wins / total_matches) * 100
    loss_percentage = (losses / total_matches) * 100
    tie_percentage = (ties / total_matches) * 100

    most_player_of_match = max(player_of_match_count, key=player_of_match_count.get)
    total_awards = player_of_match_count[most_player_of_match]

    print(f"Total Matches: {total_matches}")
    print(f"Wins: {wins}, Win Percentage: {win_percentage:.2f}%")
    print(f"Losses: {losses}, Loss Percentage: {loss_percentage:.2f}%")
    print(f"Tied: {ties}, Tie Percentage: {tie_percentage:.2f}%")
    print(f"Total Runs Scored: {total_runs}")
    print(f"Total Wickets Taken: {total_wickets}")
    print(f"Most 'Player of the Match' Awards: {most_player_of_match} with {total_awards} awards")


# Example usage:
file = 'C:\\Users\\hp\\Desktop\\PythonPractical\\Project_odi.csv' 

# Load the dataset
matches = load(file)

# Perform overall analysis
analyze_matches(matches)

