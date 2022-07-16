from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("*****                                               ******")
print("*****  THIS APP AUTOMATES WHATSAPP WEB MESSAGING    ******")
print("*****                                               ******")
print("**********************************************************")
print(style.RESET)

f = open("message.txt","r")
message = f.read()
f.close()

print('\n This is Your Message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

phone_numbers = []
f = open("phone_numbers.txt","r")
for line in f.read().splitlines():
	if line.strip() != "":
		phone_numbers.append(line.strip())
f.close()

total_phone_numbers = len(phone_numbers)
print(style.RED + 'We found ' + str(total_phone_numbers) + ' numbers in the file ' + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up web whatsapp. Sign in using QR Code')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

for idx,number in enumerate(phone_numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => sending message to {}.'.format((idx+1),total_phone_numbers,number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq']")))
				except Exception as e:
					print(style.RED + f"\n Failed to send message to {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to '+number + style.RESET)
driver.close()