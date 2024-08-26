file_path = '..\\Project_odi.csv'  

total_matches = 0
wins = 0
losses = 0
ties = 0
total_runs = 0
total_wickets = 0
player_of_match_count = {}

with open(file_path, 'r') as file:
    lines = file.readlines()
    
    for line in lines[1:]:
        parts = line.strip().split(',')
        result = parts[3]
        runs_scored = int(parts[4])
        wickets_taken = int(parts[5])
        player_of_match = parts[6]

        total_matches += 1
        if result == "Win":
            wins += 1
        elif result == "Loss":
            losses += 1
        elif result == "Tied":
            ties += 1

        total_runs += runs_scored
        total_wickets += wickets_taken

        if player_of_match in player_of_match_count:
            player_of_match_count[player_of_match] += 1
        else:
            player_of_match_count[player_of_match] = 1

if total_matches > 0:
    win_percentage = (wins / total_matches) * 100
    loss_percentage = (losses / total_matches) * 100
    tie_percentage = (ties / total_matches) * 100
else:
    win_percentage = 0
    loss_percentage = 0
    tie_percentage = 0

most_player_of_match = ''
total_awards = 0
for player, count in player_of_match_count.items():
    if count > total_awards:
        most_player_of_match = player
        total_awards = count
        
print("ODI match summary from 2016 to 2024 : \n")
print("Total Matches:",total_matches)
print("Wins:",wins,"Win Percentage: ",win_percentage,"%")
print("Losses:",losses,"Loss Percentage:",loss_percentage,"%")
print("Tied:",ties,"Tie Percentage:",tie_percentage,"%")
print("Total Runs Scored:",total_runs)
print("Total Wickets Taken:",total_wickets)
print("Most 'Player of the Match' Awards:",most_player_of_match,"with",total_awards,"awards")
