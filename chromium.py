from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller
import time

# MAIL & PASSWORD (THE MAIL YOU WILL USE TO ENTER THE MEET)
usernameStr = '200501022@student.bdu.edu.vn'
passwordStr = ''
url_meet = 'https://meet.google.com/scr-mwqk-pvs'

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,  # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(options=options)

browser.get('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier')
username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(('id', 'identifierId'))
)

username.send_keys(usernameStr)
nextButton = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(('id', 'identifierNext'))
)

nextButton.click()
time.sleep(5)

keyboard = Controller()
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(('xpath', "//input[@type='password']"))
)

password.send_keys(passwordStr)
signInButton = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(('id', 'passwordNext'))
)

signInButton.click()
time.sleep(3)

browser.get(url_meet)
time.sleep(6)
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(('class name', 'CwaK9'))
)
element.click()
browser.find_element_by_xpath("//span[text()='Ask to join']").click()

time.sleep(5)
browser.quit()
