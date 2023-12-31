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
    all_select_elements = driver.find_elements(By.CLASS_NAME, "si-selectBox")
    team_select = Select(all_select_elements[2])
    team_select.select_by_visible_text("Kolkata Knight Riders")

    # Scroll down by one screen height
    driver.execute_script("window.scrollBy(0, window.innerHeight);")

    # Click on load more button
    time.sleep(2)
    load_more_button = driver.find_element(By.CLASS_NAME, "si-action")
    load_more_button.click()

    print("Load more button clicked")

    # Select all players list
    parent_div_players = driver.find_element(By.CLASS_NAME, "si-tbl-body")
    players_list = parent_div_players.find_elements(By.CLASS_NAME, "si-tbl-row")
    count = 1
    for player in players_list:
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

        print(str(count) + "," + player_name.text + "," + player_match_div.text + "," + player_runs_div.text + "," + player_highscore_div.text + "," + player_average_div.text + "," + player_strike_rate_div.text + "," + player_100_div.text + "," + str(player_50_div.text) + "," + player_4s_div.text + "," + player_6s_div.text + "," + player_ducks_div.text + "," + str())
        count += 1


except NoSuchElementException:
    print("Whoops")

# try:
#     team_select_element = driver.find_element(By.CLASS_NAME, "si-selectBox")
#     team_select = Select(team_select_element)
#     team_select.select_by_index(6)
#     print("Team selected")
# except NoSuchElementException:
#     print("Could not select the team")
