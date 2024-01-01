import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

options = Options()
options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")  # Set the desired window size
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome(options=options)
driver.get("https://www.kkr.in/stats")

print("Starting test")
years = 16

# Getting batting data
previous_average = 0
previous_strike_rate = 0
try:
    # Get most runs
    highest_score = 0
    highest_score_player = ""
    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Runs
            player_runs_div = player.find_element(By.CLASS_NAME, "si-runs")
            if int(player_runs_div.text) > highest_score:
                highest_score = int(player_runs_div.text)
                highest_score_player = player_name.text

            # Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            print(team_name.text + "," + player_name.text + "," + str(player_runs_div.text) + ",")

    print("Highest Runs: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")

print("")
print("")
previous_ballfaced = 0
previous_strike_rate = 0
try:
    # Get Highest Score
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(1)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-bf").text != previous_ballfaced or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Highscore
            player_runs_div = player.find_element(By.CLASS_NAME, "si-hs").text.replace("*", "")
            if int(player_runs_div) > highest_score:
                highest_score = int(player_runs_div)
                highest_score_player = player_name.text

            # Balls faced
            previous_ballfaced = player.find_element(By.CLASS_NAME, "si-bf").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            print(team_name.text + "," + player_name.text + "," + str(player_runs_div) + ",")

    print("Highest Score: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")


print("")
print("")
previous_average = 0
previous_strike_rate = 0
try:
    # Get Highest Batting Average
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(2)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Batting Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text
            if float(previous_average) > highest_score and int(player_match_div.text) > 6:
                highest_score = float(previous_average)
                highest_score_player = player_name.text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            print(team_name.text + "," + player_name.text + "," + str(previous_average) + ",")

    print("Highest Average: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")


print("")
print("")
previous_average = 0
previous_strike_rate = 0
try:
    # Get Highest Strike Rate
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(3)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Batting Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text
            if float(previous_strike_rate) > highest_score and int(player_match_div.text) > 6:
                highest_score = float(previous_strike_rate)
                highest_score_player = player_name.text

            print(team_name.text + "," + player_name.text + "," + str(previous_strike_rate) + ",")

    print("Highest Strike Rate: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")


print("")
print("")
previous_average = 0
previous_strike_rate = 0
try:
    # Get Most 100s
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(4)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Batting Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            # 100s
            players_100s = player.find_element(By.CLASS_NAME, "si-100").text
            if int(players_100s) > highest_score:
                highest_score = int(players_100s)
                highest_score_player = player_name.text

            print(team_name.text + "," + player_name.text + "," + str(players_100s) + ",")

    print("Most 100s: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")


print("")
print("")
previous_average = 0
previous_strike_rate = 0
try:
    # Get Most 50s
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(5)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Batting Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            # 50s
            players_50s = player.find_element(By.CLASS_NAME, "si-50").text
            if int(players_50s) > highest_score:
                highest_score = int(players_50s)
                highest_score_player = player_name.text

            print(team_name.text + "," + player_name.text + "," + str(players_50s) + ",")

    print("Most 50s: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")


print("")
print("")
previous_average = 0
previous_strike_rate = 0
try:
    # Get Most 4s
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(6)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Batting Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            # 4s
            players_4s = player.find_element(By.CLASS_NAME, "si-4s").text
            if int(players_4s) > highest_score:
                highest_score = int(players_4s)
                highest_score_player = player_name.text

            print(team_name.text + "," + player_name.text + "," + str(players_4s) + ",")

    print("Most 4s: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")


print("")
print("")
previous_average = 0
previous_strike_rate = 0
try:
    # Get Most 6s
    highest_score = 0
    highest_score_player = ""

    # Select the highest score option
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[1])
    team_select.select_by_index(7)
    time.sleep(5)

    for year in range(0, years):
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[0])
        team_select.select_by_index(year)

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        player = players_list[0]

        # Wait for div to load
        wait_screen_loads = WebDriverWait(player, 20)
        # Use a lambda function to check if the text is not equal to previous_average
        element_found = wait_screen_loads.until(
            lambda d: d.find_element(By.CLASS_NAME, "si-ave").text != previous_average or
                      d.find_element(By.CLASS_NAME, "si-sr").text != previous_strike_rate
        )
        if element_found:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Batting Average
            previous_average = player.find_element(By.CLASS_NAME, "si-ave").text

            # Strike Rate
            previous_strike_rate = player.find_element(By.CLASS_NAME, "si-sr").text

            # 6s
            players_6s = player.find_element(By.CLASS_NAME, "si-6s").text
            if int(players_6s) > highest_score:
                highest_score = int(players_6s)
                highest_score_player = player_name.text

            print(team_name.text + "," + player_name.text + "," + str(players_6s) + ",")

    print("Most 6s: " + highest_score_player + "," + str(highest_score))
except NoSuchElementException:
    print("No results found")