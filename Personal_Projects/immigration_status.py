"""
Seeing if I can figure out how to write this unoptimized first project that I did on Java.

"""

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(executable_path=r"C:\\Users\mario\Desktop\Python-ZeroToConfident\ChromeDriver\chromedriver.exe")

def immigration_status():
    driver.get("https://egov.uscis.gov/processing-times/")
    driver.find_element_by_xpath("//*[@id=\'selectForm\']/option[7]").click()
   # time.sleep(2) #Have to learn to add wait until x = true
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='officeOrCenter']/option[2]"))).click()
    driver.find_element_by_xpath("//*[@id='getProcTimes']").click()
    time.sleep(3)
    print("Immigration is currently working on claims from:  " + driver.find_element_by_css_selector("#date").text)

time.sleep(10)
immigration_status()
