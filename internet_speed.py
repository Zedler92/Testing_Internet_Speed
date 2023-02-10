from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = "XXX"
TWITTER_PASSWORD = "XXX"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = "120"
        self.up = "120"
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(40)
        act_down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        act_up = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return [float(act_down), float(act_up)]


    def tweet_at_provider(self, act_down, act_up):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, ".r-pw2am6 div").click()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, ".public-DraftEditor-content div").send_keys(f"Hey! What is going on! Your promised 150Mbps/120Mbps, while there are only {act_down}Mbps/{act_up}Mbps!")






