from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
driver.get(url)
title=driver.title
print(f'Actual title: {title}')

login_form_header_elements=driver.find_element_by_xpath('//*[@id="login_form"]/h1')
login_form_header_text=login_form_header_elements.text
print(f'Login from header text: {login_form_header_text}')

login_input_element=driver.find_element_by_xpath('//*[@id="login_id"]')
# print(f'Input box text before send keys(): {login_input_element.text}')
# login_input_element.send_keys('kocur','132')
# print(f'Input box text after send keys(): {login_input_element.text}')


print(f'Input box text before send_keys(): {login_input_element.get_attribute("value")}')

login_input_element.send_keys('kocur13')

print(f'Input box text after send_keys(): {login_input_element.get_attribute("value")}')
login_input_element.clear()

print(f'Input box text after clear(): {login_input_element.get_attribute("value")}')

login_input_element.send_keys('1234567')
login_next_button_element = driver.find_element_by_xpath('//*[@id="login_next"]')
login_next_button_element_disabled = login_next_button_element.get_property('disabled')
print(f'Is boolean True?:  {login_next_button_element_disabled==True}')

login_input_element.clear()
login_input_element.send_keys('12345678')
login_next_button_element_disabled = login_next_button_element.get_property('disabled')
print(f'Is boolean True?:  {login_next_button_element_disabled==True}')

login_reminder_element=driver.find_element_by_xpath('//*[@id="ident_rem"]')
login_reminder_element.click()

time.sleep(3)
close_popUp=driver.find_element_by_xpath('//*[@id="shadowbox"]/div/i')
close_popUp.click()
# login_input_element.clear()
# login_input_element.send_keys('1234567')
# login_next_button_element_disabled = login_next_button_element.get_property('disabled')
# print(f'Is boolean True?:  {login_next_button_element_disabled==True}')
time.sleep(1)
driver.quit()