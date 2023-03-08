from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Twitterのログイン情報とDMの送信先を指定する
username = 'suzukibigfuck'
password = 'Yuta0110'
recipient = 'Kuro_pua'

# SeleniumのWebDriverを初期化する
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

# ユーザー名とパスワードを入力してログインする
elem = driver.find_element_by_name("session[username_or_email]")
elem.send_keys(username)
elem = driver.find_element_by_name("session[password]")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(2)

# DM画面を開く
driver.get("https://twitter.com/messages/compose?recipient_id=" + recipient)
time.sleep(2)

# DMを送信する
elem = driver.find_element_by_css_selector("div[aria-label='New message']")
elem.click()
time.sleep(2)
elem = driver.find_element_by_css_selector("div[data-testid='dmComposerTextInput']")
elem.send_keys("DM自動送信テスト。")
time.sleep(2)
elem = driver.find_element_by_css_selector("div[data-testid='dmComposerSendButton']")
elem.click()
time.sleep(2)

# WebDriverを終了する
driver.quit()
