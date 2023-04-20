from linkedin_scraper import Person, actions
from linkedin_scraper import Company
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")



company_urls = []
companies = []
for url in company_urls:
    companies.append(Company(url))


email = "aryaman_khandelwal@yahoo.com"
password = "dhinkachika2000"
actions.login(driver, email, password)
time.sleep(0.5)
rick_fox = Person("https://www.linkedin.com/in/rifox?trk=pub-pbmap", driver= driver)
iggy = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver = driver)
Anirudra = Person("https://in.linkedin.com/in/anirudra-choudhury-109635b1", driver = driver)
