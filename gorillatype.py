from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pyautogui import write
from time import sleep

## OPTIONS
options = Options()

driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)

URL = "https://typingspeedtests.com/custom-typing-test.html"
driver.get(URL)
sleep(3)
driver.find_element(By.ID, 'btn-start').click()

sleep(2)  # Wait for the page to load

words = driver.find_elements(By.CLASS_NAME, '__words')
for word in words:
    letters = word.find_elements(By.TAG_NAME, 'char')
    for letter in letters:
        write(letter.text)
sleep(10)
driver.quit()