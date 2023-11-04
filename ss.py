import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()


chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
act =ActionChains(driver)
driver.execute_script( "window.scrollBy(0,400)",'')

# ss method
# gets as pi


driver.save_screenshot("C:\\Users\ABHI\\OneDrive - RAJARAMBAPU INSTITUTE OF TECHNOLOGY\\Desktop\\SS\\automaton.png")
