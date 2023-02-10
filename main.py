from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from internet_speed import InternetSpeedTwitterBot

PROMISED_UP = 150
PROMISED_DOWN = 150

tweet_problem = InternetSpeedTwitterBot()
speed = tweet_problem.get_internet_speed()
if speed[0] < PROMISED_DOWN or speed[1] <PROMISED_UP:
    tweet_problem.tweet_at_provider(speed[0], speed[1])


