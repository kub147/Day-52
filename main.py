from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

SIMILAR_ACCOUNT = 'rozkoszny'
INSTAGRAM_EMAIL = 'mail'
INSTAGRAM_PASS = 'pass'



class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
        time.sleep(3)
    def login(self):
        log_in = self.driver.find_element(By.NAME, 'username')
        log_in.send_keys(INSTAGRAM_EMAIL)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(INSTAGRAM_PASS + Keys.ENTER)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Zapisz informacje')]").click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Nie teraz')]").click()
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//a[contains(text(), 'obserwujący')]").click()
        time.sleep(5)
        pierwsze_obs = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]')
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pierwsze_obs)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Obserwuj')]")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(random.uniform(1, 2))
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

time.sleep(30)
bot.driver.quit()