# Function to load data from CSV file
def load_data_from_csv(file_path):
    matches = []
    with open(file_path, 'r') as file:
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

# Function to analyze a single match
def analyze_single_match(match):
    scorer = match['runs_scored']
    wicket_taker = match['wickets_taken']
    player_of_match = match['player_of_match']

    print(f"Runs Scored in Match: {scorer}")
    print(f"Wickets Taken in Match: {wicket_taker}")
    print(f"Player of the Match: {player_of_match}")

# Example usage:
file_path = 'C:\\Users\\hp\\Desktop\\PythonPractical\\Project_odi.csv'  # Ensure this path is correct

# Load the dataset
matches = load_data_from_csv(file_path)

# Perform analysis on a specific match (example: first match)
analyze_single_match(matches[0])  # Replace `0` with the index of the match you want to analyze
