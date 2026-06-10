from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pg
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

location= input("Enter the location you want to search for: ")
service = input("Enter the service you want to search for: ")
data =[]
def map_data_parser(Driver,data=data):
	destination_window = Driver.find_element(by.XPATH, "//div[@class='bJzME Hu9e2e IJUlqd vJk0Jb']")
	try:
		destination_name = destination_window.find_element(by.XPATH, "//h1[@class='DUwDvf lfPIob']").text
	except:
		destination_name = None

	try:
		destination_subtitle = destination_window.find_element(by.XPATH, "//h2[@class='bwoZTb fontBodyMedium']").text
	except:
		destination_subtitle = None

	try:
		destination_type = destination_window.find_element(by.XPATH, "//div[@class='fontBodyMedium']").text
		destination_type = destination_type.replace("·\uf54a", "")
	except:
		destination_type = None

	try:
		destination_website = destination_window.find_elements(by.XPATH, "//a[@data-tooltip='Open website']")[1].get_attribute("href")
	except:
		destination_website = None

	try:
		destination_phone = destination_window.find_element(by.XPATH, "//button[@data-tooltip='Copy phone number']").text
		destination_phone = destination_phone.replace("\ue0b0\n", "")
	except:
		destination_phone = None

	try:
		destination_address = destination_window.find_element(by.XPATH, "//button[@data-tooltip='Copy address']").text
		destination_address = destination_address.replace("\ue0c8\n", "")
	except:
		destination_address = None

	try:
		destination_plus_code = destination_window.find_elements(by.XPATH, ".//button[@data-tooltip='Copy plus code']")[0].get_attribute("aria-label")
		destination_plus_code = destination_plus_code.replace("Plus code: ", "")
	except:
		print("Plus code not found")
		destination_plus_code = None

	print({
		"Destination Name": destination_name,
		"Destination subtitle": destination_subtitle,
		"Destination type": destination_type,
		"Destination website": destination_website,
		"Destination phone": destination_phone,
		"Destination address": destination_address,
		"Destination plus code": destination_plus_code
	})

	data.append({
		"Destination Name": destination_name,
		"Destination subtitle": destination_subtitle,
		"Destination type": destination_type,
		"Destination website": destination_website,
		"Destination phone": destination_phone,
		"Destination address": destination_address,
		"Destination plus code": destination_plus_code
	})

	print( "\nDestination window found" )




options = Options()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.get("https://www.google.com/maps")

time.sleep(2)

search_box = driver.find_element(by.XPATH, ".//input[@role='combobox']")
search_box.send_keys(f"{service} in {location}")  # Search text

action.send_keys(keys.ENTER).perform()  # Press Enter to search
time.sleep(4)

# Scroll down to load more results
pg.moveTo(200, 220, duration=1)
time.sleep(2)
pg.leftClick()

while True:
	action.send_keys(keys.ARROW_DOWN).perform()
	if driver.find_elements(by.XPATH, ".//div[@class='m6QErb XiKgde tLjsW eKbjU ']"): 
		print("Reached the end of the results.")
		break

destinations = driver.find_elements(by.XPATH, ".//a[@class='hfpxzc']") 
print(f"Total destinations found: {len(destinations)}")

for destination in destinations:
	driver.execute_script("arguments[0].scrollIntoView();", destination)
	time.sleep(0.5)
	destination.click()
	time.sleep(0.5)
	map_data_parser(driver)


	time.sleep(2)

pd.DataFrame(data).to_excel(f"data of {service} in {location}.xlsx", index=False)

time.sleep(20)