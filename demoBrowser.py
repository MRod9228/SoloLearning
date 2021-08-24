#TEST
#TEST 1
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\mario\Desktop\Python-ZeroToConfident\ChromeDriver\chromedriver.exe")

driver.get("https://oldschool.runescape.com/")
driver.find_element_by_link_text(link_text="Deadman: Reborn").click()
time.sleep(10)
#driver.find_element_by_xpath("//input[@title='Search']").send_keys("adaasdasds")
