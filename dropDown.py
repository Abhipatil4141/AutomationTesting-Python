import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

drp = driver.find_element(By.ID,value="drop1")

d = Select(drp)
d.select_by_visible_text("doc 1")
time.sleep(2)
d.select_by_index(3)
time.sleep(2)
d.select_by_index(0)


