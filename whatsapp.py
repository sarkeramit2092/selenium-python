from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()

# Use a dedicated, clean Chrome profile
profile_path = os.path.abspath("chrome-selenium-profile")
options.add_argument(f"user-data-dir={profile_path}")

# Optional (to reduce crashes)
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 1000)

# WhatsApp automation code
target = '"My Lady"'
message = "I Love You"
number_of_times = 10000

contact_path = f'//span[contains(@title,{target})]'
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
contact.click()

message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))

for _ in range(number_of_times):
    message_box.send_keys(message + Keys.ENTER)
    time.sleep(0.2)

input("Messages sent! Press Enter to quit...")
driver.quit()
