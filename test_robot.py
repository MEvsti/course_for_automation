
import time
import unittest
from selenium import webdriver

class TestRobot(unittest.TestCase):
 def test_robot1(self):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Я")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Робот")
    input2 = browser.find_element_by_css_selector('.form-control.third')
    input2.send_keys("Пидобот")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    self.assertEqual('Congratulations! You have successfully registered!', welcome_text)
    time.sleep(10)
    browser.quit()
 def test_robot2(self):
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Я")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Робот")
    input2 = browser.find_element_by_css_selector('.form-control.third')
    input2.send_keys("Пидобот")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    self.assertEqual('Congratulations! You have successfully registered!', welcome_text)
    time.sleep(10)
    browser.quit()
if __name__ == "__main__": unittest.main()