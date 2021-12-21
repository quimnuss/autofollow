import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import selenium.webdriver.support.ui as ui

# from webdriver_manager.firefox import GeckoDriverManager

creadors = ['creadorstv']

# new_driver_path = r'C:\Users\Public\geckodriver.exe'
# new_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# ops = Options()
# ops.binary_location = new_binary_path
# driver = webdriver.Firefox(options=ops,executable_path=GeckoDriverManager().install())
# driver = webdriver.Firefox(executable_path= r'C:\Program Files\Mozilla Firefox\firefox.exe')
# this works
# driver = webdriver.Firefox(executable_path= r'C:\Users\Public\geckodriver.exe')
driver = webdriver.Firefox(executable_path= r'geckodriver.exe')
# binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary)

driver.maximize_window()

driver.get("http://www.twitch.tv/")
wait = ui.WebDriverWait(driver, 60)

driver.get("http://www.twitch.tv/user/login")
driver.find_element_by_css_selector('button[data-a-target="login-button"]').click()
time.sleep(40)
wait.until(lambda driver: driver.find_element_by_css_selector('button[data-a-target="top-nav-get-bits-button"]'))
for creador in creadors:
    driver.get("http://www.twitch.tv/{}".format(creador))
    follow_button = driver.find_element_by_css_selector('button[data-a-target="follow-button"]')
    if follow_button:
        follow_button.click()
    else:
        print("Follow button for {} not found. You might be a follower already.".format(creador))

driver.quit()

print("Job's Done, Have a Nice Day!")