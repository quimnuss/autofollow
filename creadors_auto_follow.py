import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.ui as ui

with open("streamer_list.txt", "r") as f:
    content = f.read()
    creadors = content.split('\n')

service = Service('geckodriver.exe')
driver = webdriver.Firefox(service=service)

driver.maximize_window()

driver.get("http://www.twitch.tv/")
wait = ui.WebDriverWait(driver, 60)

driver.get("http://www.twitch.tv/user/login")
driver.find_element(By.CSS_SELECTOR, 'button[data-a-target="login-button"]').click()
time.sleep(30)
wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR,
                                              'button[data-a-target="top-nav-get-bits-button"]'))

num_creadors = len(creadors)
for i, creador in enumerate(creadors):
    driver.get("http://www.twitch.tv/{}".format(creador))
    follow_button = driver.find_element(By.CSS_SELECTOR, 'button[data-a-target="follow-button"]')
    if follow_button:
        follow_button.click()
        print("Followed {} {}/{}".format(creador, i + 1, num_creadors))
    else:
        print("Follow button for {} not found. You might be a follower already.".format(creador))

driver.quit()

print("Job's Done, Have a Nice Day!")