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

# drag-drop operation
source=driver.find_element(By.XPATH ,value='//*[@id="draggable"]')
target= driver.find_element(By.XPATH,value='//*[@id="droppable"]')

act.drag_and_drop(source,target).perform()
