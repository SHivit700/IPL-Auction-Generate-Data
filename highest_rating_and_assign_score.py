# Reading from bowling_data_with_rating.txt and batting_ratting.txt and creating a new doc to store score of players
import csv

bowling_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/bowling_data_with_rating.txt'
batting_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/batting_data_with_rating.txt'
batting_final_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/batting_score_final.txt'
bowling_final_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/bowling_score_final.txt'

ratings_bowling = []

# Open the file and read it as CSV
with open(bowling_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        bowling_rating = float(row[13])
        ratings_bowling.append(bowling_rating)

min_rating = min(ratings_bowling)
adjusted_ratings = [rating - min_rating for rating in ratings_bowling]
max_adjusted_rating = max(adjusted_ratings)
normalized_ratings = [(round((rating / max_adjusted_rating) * 40, 2) + 60) for rating in adjusted_ratings]
# print(normalized_ratings)

count = 0

# Open the same file and read it as CSV
with open(bowling_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    with open(bowling_final_file_path, 'w') as write_file:
        # Iterate over each row in the CSV
        for row in csv_reader:
            team = row[0]
            player_name = row[1]
            match = int(row[2])
            overs = float(row[3])
            maidens = int(row[4])
            runs = int(row[5])
            wickets = int(row[6])
            bbi = row[7]
            average = float(row[8])
            economy_rate = float(row[9])
            strike_rate = float(row[10])
            three_wickets = int(row[11])
            five_wickets = int(row[12])
            normalized_ratings[count] = round(normalized_ratings[count])

            write_file.write((team + "," + player_name + "," + str(match) + "," + str(overs) + "," + str(maidens) + ","
                              + str(runs) + "," + str(wickets) + "," + bbi + "," + str(average) + "," +
                              str(economy_rate) + "," + str(strike_rate) + "," + str(three_wickets) + "," +
                              str(five_wickets) + "," + str(round(normalized_ratings[count])) + ",\n"))
            # if normalized_ratings[count] >= 80:
            #     print(team + "," + player_name + "," + str(match) + "," + str(overs) + "," + str(maidens) + "," + str(runs)
            #           + "," + str(wickets) + "," + bbi + "," + str(average) + "," + str(economy_rate) + "," +
            #           str(strike_rate) + "," + str(three_wickets) + "," + str(five_wickets) + "," +
            #           str(round(normalized_ratings[count])) + ",")
            # if normalized_ratings[count] >= 80:
            #     print(str(player_name) + "," + str(normalized_ratings[count]))
            count += 1

print(" ")
print(" ")
print(" ")

# Batting
ratings_batting = []
runs_batting = []

# Open the file and read it as CSV
with open(batting_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        batting_rating = float(row[13])
        batting_runs = float(row[14])
        ratings_batting.append(batting_rating)
        runs_batting.append(batting_runs)

min_rating = min(ratings_batting)
adjusted_ratings = [rating - min_rating for rating in ratings_batting]
max_adjusted_rating = max(adjusted_ratings)
normalized_ratings = [(round((rating / max_adjusted_rating) * 40, 2) + 60) for rating in adjusted_ratings]

min_rating = min(runs_batting)
adjusted_ratings = [runs - min_rating for runs in runs_batting]
max_adjusted_rating = max(adjusted_ratings)
normalized_ratings_runs = [(round((runs / max_adjusted_rating) * 55, 2) + 5) for runs in adjusted_ratings]
# print(normalized_ratings)

count = 0

# Open the same file and read it as CSV
with open(batting_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    with open(batting_final_file_path, 'w') as write_file:
        # Iterate over each row in the CSV
        for row in csv_reader:
            team = row[0]
            player_name = row[1]
            match = int(row[2])
            overs = float(row[3])
            maidens = int(row[4])
            runs = int(row[5])
            wickets = float(row[6])
            bbi = row[7]
            average = float(row[8])
            economy_rate = float(row[9])
            strike_rate = float(row[10])
            three_wickets = int(row[11])
            five_wickets = int(row[12])
            normalized_ratings[count] = round(normalized_ratings[count])
            normalized_ratings_runs[count] = round(normalized_ratings_runs[count])

            write_file.write(team + "," + player_name + "," + str(match) + "," + str(overs) + "," + str(maidens) + ","
                             + str(runs) + "," + str(wickets) + "," + bbi + "," + str(average) + "," + str(economy_rate)
                             + "," + str(strike_rate) + "," + str(three_wickets) + "," + str(five_wickets) + "," +
                             str(round(normalized_ratings[count])) + "," + str(
                round(normalized_ratings_runs[count])) + ",\n")
            # print(team + "," + player_name + "," + str(match) + "," + str(overs) + "," + str(maidens) + "," + str(runs)
            #       + "," + str(wickets) + "," + bbi + "," + str(average) + "," + str(economy_rate) + "," +
            #       str(strike_rate) + "," + str(three_wickets) + "," + str(five_wickets) + "," +
            #       str(round(normalized_ratings[count])) + ",")
            # if normalized_ratings[count] >= 90:
            #     print(str(player_name) + "," + str(normalized_ratings[count]) + "," + str(normalized_ratings_runs[count]))
            count += 1

# Combine bowling and batting ratings
# TEAM
# PLAYER
# MAT
# OVR
# MAIDEN
# RUNS
# WKT
# BBI
# AVG
# ECON
# S/R
# 3W
# 5W
# RATING
# ,
# MAT
# NO
# RUNS
# HS
# AVG
# S/R
# 100s
# 50s
# 4s
# 6s
# DUCKS
# RATING
# RUNS WHEN NOT OUT

# File paths
batting_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/batting_score_final.txt'
bowling_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/bowling_score_final.txt'
combined_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/cricket-web-app/public/combined_rating_final.txt'
combined_file_path_with_fantasy_value = '/Users/shivit/Desktop/Lab/webTester/dataIPL/cricket-web-app/public/combined_file_path_with_fantasy_value.txt'

# Read data into dictionaries
bowling_data = {}
with open(bowling_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        bowling_data[row[1]] = row  # key is player's name

batting_data = {}
with open(batting_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        batting_data[row[1]] = row

# Combine data
combined_data = []
for player, data in bowling_data.items():
    if player in batting_data:
        combined_row = data + batting_data[player][2:]  # Skip team and player name for batting data
    else:
        # Default batting values for players not in batting dataset
        combined_row = data + ['0'] * 11  # Adjust the number of '0's based on number of batting columns
        combined_row = combined_row + ['40', '1', '']  # Default of 25 batting rating and 1 run
    combined_data.append(combined_row)

# Add remaining batting players
for player, data in batting_data.items():
    if player not in bowling_data:
        # Default bowling values for players not in bowling dataset
        default_bowling = ['0'] * 11 + ['40', '']  # Adjust the number of '0's based on number of bowling columns
        combined_row = data[:2] + default_bowling + data[2:]  # Default bowling rating of 25
        combined_data.append(combined_row)

# Write to final file
with open(combined_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for row in combined_data:
        csv_writer.writerow(row)

print("")
print("")

with (open(combined_file_path, 'r') as file):
    csv_reader = csv.reader(file)
    total_fantasy = 0
    players = 0

    with open(combined_file_path_with_fantasy_value, 'w') as write_file:
        for row in csv_reader:
            s1 = row[0]
            s2 = row[1]
            s3 = row[2]
            s111 = row[3]
            s4 = row[4]
            s5 = row[5]
            s6 = row[6]
            s7 = row[7]
            s8 = row[8]
            s9 = row[9]
            s10 = row[10]
            s11 = row[11]
            s12 = row[12]
            s13 = int(row[13])  # Bowling
            s14 = row[14]
            s15 = row[15]
            s16 = row[16]
            s17 = row[17]
            s18 = row[18]
            s19 = row[19]
            s20 = row[20]
            s21 = row[21]
            s22 = row[22]
            s23 = row[23]
            s24 = row[24]
            s25 = row[25]
            s26 = int(row[26])  # Batting
            runs_scored = int(row[27])  # Runs Scored

            batting_weight = 0.6
            bowling_weight = 0.4
            runs_weight = 0.2
            max_runs = 60

            # Modifier based on ratings and runs
            modifier = 1.0

            # Highly rated batsmen get a higher modifier
            if s26 >= 95 or (s26 >= 90 and runs_scored >= max_runs * 3 / 4) or runs_scored >= max_runs * 5 / 6:
                modifier = 1.15
            # Just bowlers get a slight boost due to algorithm favouring runs_scored
            elif s13 >= 85 and s26 <= 50:
                modifier = 1.5
            # All-rounders get a higher modifier
            elif (s26 >= 90 and s13 >= 80) or (s26 >= 80 and s13 >= 90) or (s13 >= 90 and runs_scored >= max_runs / 2):
                modifier = 1.08
            elif s26 >= 90 and s13 >= 70:
                modifier = 1.08
            elif s26 >= 90 or s13 >= 90:
                modifier = 1.08
            elif (s26 >= 80 and s13 >= 75) or (s26 >= 75 and s13 >= 80) or \
                    (s26 >= 75 and runs_scored >= max_runs / 2) or (s13 >= 75 and runs_scored >= max_runs / 2):
                modifier = 1.01
            elif s13 >= 80 and s26 <= 50:
                modifier = 1.02
            elif s26 < 80 and s13 < 80 and runs_scored <= max_runs / 2:
                modifier = 0.8
            # Players with no rating above 70 are half the price of players above 95 in any category
            elif s26 <= 70 and s13 <= 70 and runs_scored <= max_runs / 2:
                modifier = 0.5

            # Calculate fantasy value
            fantasy_value = (s26 * batting_weight + s13 * bowling_weight + runs_scored * runs_weight) * modifier

            # Cap the fantasy value between 5 and 200
            fantasy_value = max(5, min(200, int(fantasy_value)))

            if fantasy_value > 40:
                print(str(s1) + "," + str(s2) + "," + str(s13) + "," + str(s26) + "," + str(runs_scored) + "," + str(
                    fantasy_value))

            write_file.write(str(s1) + "," + str(s2) + "," + str(s111) + "," + str(s3) + "," + str(s4) + "," + str(s5)
                             + "," + str(s6) + "," + str(s7) + "," + str(s8) + "," + str(s9) + "," + str(s10) + "," +
                             str(s11) + "," + str(s12) + "," + str(s13) + "," + str(s14) + "," + str(s15) + "," +
                             str(s16) + "," + str(s17) + "," + str(s18) + "," + str(s19) + "," + str(s20) + "," +
                             str(s21) + "," + str(s22) + "," + str(s23) + "," + str(s24) + "," + str(s25) + "," +
                             str(s26) + "," + str(runs_scored) + "," + str(fantasy_value) + ",\n")

            players += 1
            total_fantasy += fantasy_value

        print("Total value: " + str(total_fantasy) + ", total players: " + str(players) + ", per team fantasy value: " + str(total_fantasy * 11 /players))

# total 27
