⚠️ Important Notes Before Starting:
WhatsApp Web is not meant to be automated this way — so use responsibly and ethically.

Your account can be temporarily or permanently banned if WhatsApp detects bot-like behavior.

Make sure you're using this only in groups where it's allowed or part of a harmless personal project.

✅ Project Plan: WhatsApp Auto-Hola Sender

📌 Requirements:
Python

Selenium

Chrome WebDriver  https://googlechromelabs.github.io/chrome-for-testing/#stable

QR-code login on WhatsApp Web

```bash
pip install selenium==4.0.0.b4
```

🛠️ Step-by-Step Logic
Open WhatsApp Web via Selenium.
Scan the QR code manually.
Locate the specific group(s).
Send "Hola" message every 10 minutes using time.sleep(600).

🧑‍💻 Sample Code (Python + Selenium):

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Scan QR Code and press Enter...")

# List of group names
groups = ["Family", "DevOps Team"]

def send_hola(group_name):
    # Search and open group chat
    search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(2)
    
    # Click the group from the search results
    group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
    group.click()
    time.sleep(1)
    
    # Type message
    msg_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
    msg_box.send_keys("Hola")
    
    # Send the message
    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_btn.click()
    time.sleep(1)

# Loop to send messages every 10 minutes
while True:
    for group in groups:
        send_hola(group)
    print("Message sent to all groups. Waiting 10 minutes...")
    time.sleep(600)  # 10 minutes
```
🧩 Tips:
You can run this script using a background scheduler (e.g., cron on Linux or Task Scheduler on Windows).

To stop it, just Ctrl + C in terminal or close the browser.

If you want to send different messages at different times, that can also be added.