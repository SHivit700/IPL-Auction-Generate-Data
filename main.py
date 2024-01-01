import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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

# Getting batting data
try:
    for team in range(1, 10):
        # print(team)
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[2])
        team_select.select_by_index(team)
        # team_select.select_by_visible_text(team)

        # Click on load more button
        for i in range(0, 2):
            # Scroll down by one screen height
            driver.execute_script("window.scrollBy(0, 800)")
            time.sleep(2)
            try:
                load_more_button = driver.find_element(By.CLASS_NAME, "si-action")
                load_more_button.click()
            except NoSuchElementException as e:
                pass

        # print("Load more button clicked")

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        for player in players_list:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Not Outs
            player_not_out_div = player.find_element(By.CLASS_NAME, "si-no")

            # Runs
            player_runs_div = player.find_element(By.CLASS_NAME, "si-runs")

            # Highscore
            player_highscore_div = player.find_element(By.CLASS_NAME, "si-hs")

            # Average
            player_average_div = player.find_element(By.CLASS_NAME, "si-ave")

            # Strike Rate
            player_strike_rate_div = player.find_element(By.CLASS_NAME, "si-sr")

            # 100s
            player_100_div = player.find_element(By.CLASS_NAME, "si-100")

            # 50s
            player_50_div = player.find_element(By.CLASS_NAME, "si-50")

            # 4s
            player_4s_div = player.find_element(By.CLASS_NAME, "si-4s")

            # 6s
            player_6s_div = player.find_element(By.CLASS_NAME, "si-6s")

            # Ducks
            player_ducks_div = player.find_element(By.CLASS_NAME, "si-st")

            print(team_name.text + "," + player_name.text + "," + player_match_div.text + "," + player_not_out_div.text
                  + "," + player_runs_div.text + "," + player_highscore_div.text.replace('*', '') + "," +
                  player_average_div.text.replace("-", player_highscore_div.text.replace('*', '')) + ","
                  + player_strike_rate_div.text + "," + player_100_div.text + "," + str(player_50_div.text) + "," +
                  player_4s_div.text + "," + player_6s_div.text + "," + player_ducks_div.text + "," + str())

        # Scroll up by two window height
        for i in range(0, 3):
            driver.execute_script("window.scrollBy(0, -800)")
except NoSuchElementException:
    print("Whoops")

print(" ")
print(" ")
print(" ")

# Getting bowling data
# Switching to bowling tab
try:
    bowling_button = driver.find_elements(By.CLASS_NAME, "si-tab")
    bowling_button[1].click()
except NoSuchElementException:
    print("Error switching to bowling tab")

# Getting bowling data
try:
    for team in range(1, 10):
        # print(team)
        all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
        team_select = Select(all_select_elements[2])
        team_select.select_by_index(team)
        # team_select.select_by_visible_text(team)

        # Click on load more button
        for i in range(0, 2):
            # Scroll down by one screen height
            driver.execute_script("window.scrollBy(0, 800)")
            time.sleep(2)
            try:
                load_more_button = driver.find_element(By.CLASS_NAME, "si-action")
                load_more_button.click()
            except NoSuchElementException as e:
                pass

        # print("Load more button clicked")

        # Select all players list
        parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
        players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
        for player in players_list:
            # Team Name
            team_name_div = player.find_element(By.CLASS_NAME, "si-player")
            team_div = team_name_div.find_element(By.CLASS_NAME, "si-team-name")
            team_name = team_div.find_element(By.CLASS_NAME, "si-fullName")

            # Name
            player_name_div = player.find_element(By.CLASS_NAME, "si-player")
            player_name = player_name_div.find_element(By.CLASS_NAME, "si-fullName")

            # Matches
            player_match_div = player.find_element(By.CLASS_NAME, "si-mat")

            # Overs
            player_overs_div = player.find_element(By.CLASS_NAME, "si-overs")

            # Maidens
            player_maidens_div = player.find_element(By.CLASS_NAME, "si-maidens")

            # Runs
            player_runs_div = player.find_element(By.CLASS_NAME, "si-runs")

            # Wickets
            player_wickets_div = player.find_element(By.CLASS_NAME, "si-wkts")

            # BBI
            player_bbi_div = player.find_element(By.CLASS_NAME, "si-bbi")

            # Average
            player_average_div = player.find_element(By.CLASS_NAME, "si-ave")

            # Economy
            player_economy_div = player.find_element(By.CLASS_NAME, "si-econ")

            # Strike Rate
            player_strike_rate_div = player.find_element(By.CLASS_NAME, "si-sr")

            # 3W
            player_3w_div = player.find_element(By.CLASS_NAME, "si-3w")

            # 5W
            player_5w_div = player.find_element(By.CLASS_NAME, "si-5w")

            print(team_name.text + "," + player_name.text + "," + player_match_div.text + "," + player_overs_div.text + "," + player_maidens_div.text + "," + player_runs_div.text + "," + player_wickets_div.text + "," + player_bbi_div.text + "," + player_average_div.text + "," + player_economy_div.text + "," + player_strike_rate_div.text + "," + player_3w_div.text + "," + player_5w_div.text + ",")

        # Scroll up by two window height
        for i in range(0, 3):
            driver.execute_script("window.scrollBy(0, -800)")
except NoSuchElementException:
    print("Whoops")
