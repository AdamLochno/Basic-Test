import time
import unittest
from selenium import webdriver


class LoginPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_demo_login(self):
        # print('Działam')
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver = self.driver
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')

        login_form_header_element = driver.find_element_by_xpath('//*[@id="login_form"]/h1')
        login_form_header_text = login_form_header_element.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', login_form_header_text,
                         f'Expected title differ from actual title for page url: {url}')

    def test_button_dalej_is_disabled_when_login_input_is_empty(self):
        # print('Działam1')
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        # Check next button
        login_next_button_element = driver.find_element_by_xpath('//*[@id="login_next"]')
        login_next_button_element_disabled = login_next_button_element.get_property('disabled')
        print(f'Is Button disabled?:  {login_next_button_element_disabled == True}')
        self.assertEqual(True, login_next_button_element_disabled,
                         f'Expected state of button: True, got:{login_next_button_element_disabled}')


    def test_what_happens_when_login_is_too_short (self):
        driver=self.driver
        url='https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_input_element = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_input_element.clear()
        login_input_element.send_keys(1234567)
        login_input_question_mark=driver.find_element_by_xpath('//*[@id="login_id_container"]/div[3]/div/i')
        login_input_question_mark.click()
        warning_message=driver.find_element_by_xpath('//*[@class="error"]')
        warning_message_text=warning_message.text
        self.assertEqual('identyfikator ma min. 8 znaków', warning_message_text,
                    f'Expected warning message differ from actual one for url: {url}')
    def test_button_dalej_is_disabled_when_login_input_is_filled(self):
        # print('Działam2')
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_input_element = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_input_element.clear()
        login_input_element.send_keys(12345678)
        login_next_button_element = driver.find_element_by_xpath('//*[@id="login_next"]')
        time.sleep(3)
        login_next_button_element_disabled = login_next_button_element.get_property('disabled')
        print(f'Is Button disabled?:  {login_next_button_element_disabled == True}')
        login_next_button_element.click()
        time.sleep(3)
        name_of_the_website=driver.current_url
        print(f'nazwa strony: {name_of_the_website}')
        self.assertEqual('https://demobank.jaktestowac.pl/logowanie_etap_2.html?login=12345678', name_of_the_website,
                         f'Nie działa poprawnie')
        # self.assertEqual(False, login_next_button_element_disabled,
        #                  f'Expected state of button: False, got:{login_next_button_element_disabled}')