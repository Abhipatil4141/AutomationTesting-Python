import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/umesh/Upload%20and%20Download.html")
driver.maximize_window()

act = ActionChains(driver)
driver.maximize_window()

# download file
driver.find_element(By.XPATH, value='//*[@id="downloadButton"]').click()

# upload file

ab = driver.find_element(By.XPATH , value='//*[@id="uploadFile"]')
ab.send_keys("C:\\Users\\ABHI\\OneDrive - RAJARAMBAPU INSTITUTE OF TECHNOLOGY\Pictures\\793bb0d8845f9a44f922b1903fb94c58.jpg")

