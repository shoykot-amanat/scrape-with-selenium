from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path = r"C:\Users\Lenovo\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge()
driver.get(website)
all_matches_button = driver.find_element(By.XPATH, value='//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')
time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, value='tr')
date = []
home_team = []
score = []
away_team = []
for match in matches:
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index=False)
# time.sleep(10)
# driver.quit()


