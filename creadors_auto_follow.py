import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import selenium.webdriver.support.ui as ui

with open("streamer_list.txt", "r") as f:
    content = f.read()
    creadors = content.split('\n')

service = Service('geckodriver.exe')
driver = webdriver.Firefox(service=service)

driver.maximize_window()

driver.get("http://www.twitch.tv/")
long_wait = ui.WebDriverWait(driver, 60)
short_wait = ui.WebDriverWait(driver, 10)

driver.get("http://www.twitch.tv/user/login")
driver.find_element(By.CSS_SELECTOR, 'button[data-a-target="login-button"]').click()
time.sleep(30)
long_wait.until(lambda driver: driver.find_element(
    By.CSS_SELECTOR, 'button[data-a-target="top-nav-get-bits-button"]'))

num_creadors = len(creadors)
for i, creador in enumerate(creadors):
    driver.get("http://www.twitch.tv/{}".format(creador))
    time.sleep(1)
    try:
        short_wait.until(lambda driver: driver.find_element(
            By.CSS_SELECTOR, 'button[data-a-target="notifications-toggle"]'))
        follow_button = driver.find_element(By.CSS_SELECTOR,
                                            'button[data-a-target="follow-button"]')
        follow_button.click()
        print("Followed {} {}/{}".format(creador, i + 1, num_creadors))
    except NoSuchElementException:
        print("Follow button for {} not found. You might be a follower already.".format(creador))
    except TimeoutException:
        print("Timeout searching for the notification bell from {}".format(creador))

driver.quit()

print("Job's Done, Have a Nice Day!")