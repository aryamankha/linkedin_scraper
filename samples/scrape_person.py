import os
from linkedin_scraper import Person, actions
from selenium import webdriver

'''options = webdriver.ChromeOptions()

options.add_argument("--no-sandbox")
options.add_argument('--disable-gpu')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument(r"--user-data-dir=/Users/karyaman/Library/Application Support/Google/Chrome/Default")'''
driver = webdriver.Chrome("./chromedriver")

email = "otherjunk2000@gmail.com"
password = "Stallions5!"

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
rick_fox = Person("https://www.linkedin.com/in/rifox?trk=pub-pbmap")
