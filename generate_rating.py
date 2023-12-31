# Reading from bowling_data.txt and batting_data.txt and creating a new doc to store ratings of players
import csv

bowling_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/bowling_data.txt'
batting_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/batting_data.txt'

# Calculating batting score
max_runs = 890
max_score = 129
max_avg = 69
max_sr = 216.66
max_hundreds = 3
max_fifties = 8
max_4s = 85
max_6s = 36

# Open the file and read it as CSV
with open(batting_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        if row:  # Check if the row is not empty
            team_name = row[0]
            player_name = row[1]
            player_match_div = int(row[2])
            player_not_out_div = int(row[3])
            player_runs_div = int(row[4])
            player_highscore_div = int(row[5])
            player_average_div = float(row[6])
            player_strike_rate_div = float(row[7])
            player_100_div = int(row[8])
            player_50_div = int(row[9])
            player_4s_div = int(row[10])
            player_6s_div = int(row[11])
            player_ducks_div = int(row[12])

            # Calculate the bowling rating
            # Normalizing each factor (assuming higher is better for simplicity, except for economy and average)
            normalized_runs = player_runs_div / max_runs
            normalized_score = player_highscore_div / max_score
            normalized_average = player_average_div / max_avg
            normalized_strike_rate = player_strike_rate_div / max_sr
            normalized_100 = player_100_div / max_hundreds
            normalized_50 = player_50_div / max_fifties
            normalized_4s = player_4s_div / max_4s
            normalized_6s = player_6s_div / max_6s

            # Weighing each factor
            score = (normalized_runs * 53) + \
                    (normalized_score * 10) + \
                    (normalized_average * 5) + \
                    (normalized_strike_rate * 7) + \
                    (normalized_100 * 10) + \
                    (normalized_50 * 5) + \
                    (normalized_4s * 2) + \
                    (normalized_6s * 3) - \
                    (player_ducks_div * 5)

            rating = score * 100  # Scale to 100

            print(team_name + "," + player_name + "," + str(player_match_div) + "," + str(player_not_out_div)
                  + "," + str(player_runs_div) + "," + str(player_highscore_div) + "," + str(player_average_div) + ","
                  + str(player_strike_rate_div) + "," + str(player_100_div) + "," + str(player_50_div) + "," +
                  str(player_4s_div) + "," + str(player_6s_div) + "," + str(player_ducks_div) + "," + str(rating))

            # Print the player's name and their rating
            # if rating > 0:
            #     print(player_name)
            # print(str(rating) + " " + str(average) + " " + str(economy_rate))
            # print(f"{player_name} from {team} has a rating of {rating}")
print(" ")
print(" ")
print(" ")


# Calculating bowling score
# Ensure if bowler has economy 0 then assign max_economy to him
max_wickets = 28
max_economy = 6.25
max_average = 11.81
max_five_w = 1
max_three_w = 5
max_maidens = 3
max_strike_rate = 8.72

# Open the file and read it as CSV
with open(bowling_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in csv_reader:
        if row:  # Check if the row is not empty
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

            # Calculate the bowling rating
            # Normalizing each factor (assuming higher is better for simplicity, except for economy and average)
            normalized_wickets = wickets / max_wickets
            normalized_economy = 1 - (economy_rate / max_economy)  # Lower economy is better
            normalized_average = 1 - (average / max_average)  # Lower average is better
            normalized_five_w = five_wickets / max_five_w
            normalized_three_w = three_wickets / max_three_w
            normalized_maidens = maidens / max_maidens
            normalized_strike_rate = strike_rate / max_strike_rate

            # Weighing each factor
            score = (normalized_wickets * 45) + \
                    (normalized_economy * 20) + \
                    (normalized_average * 10) + \
                    (normalized_five_w * 10) + \
                    (normalized_three_w * 5) + \
                    (normalized_maidens * 5) + \
                    (normalized_strike_rate * 5)

            rating = score * 100  # Scale to 100

            print(team + "," + player_name + "," + str(match) + "," + str(overs) + "," + str(maidens) + "," + str(runs)
                  + "," + str(wickets) + "," + bbi + "," + str(average) + "," + str(economy_rate) + "," +
                  str(strike_rate) + "," + str(three_wickets) + "," + str(five_wickets) + "," + str(rating) + ",")

            # Print the player's name and their rating
            # if rating > 0:
            #     print(player_name)
            # print(str(rating) + " " + str(average) + " " + str(economy_rate))
            # print(f"{player_name} from {team} has a rating of {rating}")
