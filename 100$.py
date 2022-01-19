import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 12).until(
 EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button.click()
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id("input_value").text
y = calc(x)
entry_field = browser.find_element_by_id("answer")
entry_field.send_keys(y)
button2 = browser.find_element_by_css_selector('[type = "submit"]')
button2.click()
time.sleep(10)
browser.quit()