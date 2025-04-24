from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = "D:/python/selenium/chromedriver.exe"
s = Service(path)

driver = webdriver.Chrome(service = s)

driver.get("https://web.whatsapp.com")
input("Scan the QR code on WhatsApp Web and press Enter here...")

group_names = ["Movie recommendations group..💣💣..!!!!"] 

def send_message_to_group(group_name, message):
    try:
        search_box = driver.find_element(By.XPATH, f'//*[@id="side"]/div[1]/div/div[2]/button')
        search_box.clear()
        search_box.send_keys(group_name)
        time.sleep(2)

       
        group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
        group.click()
        time.sleep(2)

        
        msg_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
        msg_box.send_keys(message)

        
        send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_btn.click()
        print(f"Sent '{message}' to {group_name}")
    except Exception as e:
        print(f"Error sending to {group_name}: {e}")


while True:
    for group in group_names:
        send_message_to_group(group, "Hola")
    time.sleep(600) 
