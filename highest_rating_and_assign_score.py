# Reading from bowling_rating.txt and batting_ratting.txt and creating a new doc to store score of players
import csv

bowling_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/bowling_rating.txt'
batting_file_path = '/Users/shivit/Desktop/Lab/webTester/dataIPL/batting_rating.txt'

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
normalized_ratings = [(round((rating / max_adjusted_rating) * 70, 2) + 30)for rating in adjusted_ratings]
print(normalized_ratings)

count = 0

# Open the same file and read it as CSV
with open(bowling_file_path, 'r') as file:
    csv_reader = csv.reader(file)

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

        print(team + "," + player_name + "," + str(match) + "," + str(overs) + "," + str(maidens) + "," + str(runs)
              + "," + str(wickets) + "," + bbi + "," + str(average) + "," + str(economy_rate) + "," +
              str(strike_rate) + "," + str(three_wickets) + "," + str(five_wickets) + "," +
              str(round(normalized_ratings[count])) + ",")
        count += 1
