import csv

combined_rating_file_path = "/Users/shivit/Desktop/Lab/webTester/dataIPL/combined_rating_final.txt"

teams = ["Gujarat Titans",
         "Chennai Super Kings",
         "Lucknow Super Giants",
         "Mumbai Indians",
         "Rajasthan Royals",
         "Royal Challengers Bangalore",
         "Kolkata Knight Riders",
         "Punjab Kings",
         "Delhi Capitals"]
team_a = teams[0]
team_b = teams[6]

player_data_team_a = {}
player_data_team_b = {}

with open(combined_rating_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        if row[0] == team_a:
            player_name = row[1]
            player_info = {
                'team_name': row[0],
                'wickets': int(row[6]),
                'bbi': row[7],
                'econ': float(row[9]),
                'three_w': int(row[11]),
                'five_w': int(row[12]),
                'bowling_rating': int(row[13]),
                'total_runs': int(row[17]),
                'highscore': int(row[18]),
                'strike_rate': float(row[20]),
                'fifties': (row[23]),
                'hundreds': (row[24]),
                'batting_rating': int(row[26]),
                'runs_scored': int(row[27])
            }
            player_data_team_a[player_name] = player_info

        elif row[0] == team_b:
            player_name = row[1]
            player_info = {
                'team_name': row[0],
                'wickets': int(row[6]),
                'bbi': row[7],
                'econ': float(row[9]),
                'three_w': int(row[11]),
                'five_w': int(row[12]),
                'bowling_rating': int(row[13]),
                'total_runs': int(row[17]),
                'highscore': int(row[18]),
                'strike_rate': float(row[20]),
                'fifties': (row[23]),
                'hundreds': (row[24]),
                'batting_rating': int(row[26]),
                'runs_scored': int(row[27]),
                'selected_in_team': False
            }
            player_data_team_b[player_name] = player_info


# Selecting team a
def select_team(player_data):
    # Sort players by batting and bowling ratings, and then by runs scored
    sorted_players = sorted(player_data.items(),
                            key=lambda x: (x[1]['batting_rating'], x[1]['bowling_rating'], x[1]['runs_scored']),
                            reverse=True)

    # Initialize the selected team
    playing_team_a = {}

    # Define the rating thresholds
    rating_thresholds = [95, 90, 87, 85, 84, 82, 80]
    all_rounder_thresholds = [180, 175, 170, 165, 160, 155, 150]
    count = 0
    for threshold in rating_thresholds:
        for player_name, player_info in sorted_players:
            # Check if player meets the rating threshold in either batting or bowling
            total_score = player_info['batting_rating'] + player_info['bowling_rating']
            if (player_info['batting_rating'] >= threshold or player_info['bowling_rating'] >= threshold) \
                    or total_score > all_rounder_thresholds[count]:
                # Add the player to the team
                playing_team_a[player_name] = player_info

                # Check if we have selected 11 players
                if len(playing_team_a) == 11:
                    return playing_team_a
        count += 1

    # If less than 11 players are selected after checking all thresholds, add remaining top players
    for player_name, player_info in sorted_players:
        if player_name not in playing_team_a:
            playing_team_a[player_name] = player_info
            if len(playing_team_a) == 11:
                break

    return playing_team_a



# Selecting team a
playing_team_a_unsorted = select_team(player_data_team_a)
playing_team_a = dict(sorted(playing_team_a_unsorted.items(), key=lambda x: (x[1]['runs_scored'], x[1]['batting_rating'], x[1]['bowling_rating']), reverse=True))

for player in playing_team_a:
    player_info = playing_team_a[player]
    bowling_rating = player_info['bowling_rating']
    batting_rating = player_info['batting_rating']
    print(
        str(player) + ": " + str(bowling_rating) + ", " + str(batting_rating) + ", " + str(player_info['runs_scored']))

print("")
print("")

# Selecting team b
playing_team_b_unsorted = select_team(player_data_team_b)
playing_team_b = dict(sorted(playing_team_b_unsorted.items(), key=lambda x: (x[1]['runs_scored'], x[1]['batting_rating'], x[1]['bowling_rating']), reverse=True))

for player in playing_team_b:
    player_info = playing_team_b[player]
    bowling_rating = player_info['bowling_rating']
    batting_rating = player_info['batting_rating']
    print(
        str(player) + ": " + str(bowling_rating) + ", " + str(batting_rating) + ", " + str(player_info['runs_scored']))


# With teams selected, simulate the game
