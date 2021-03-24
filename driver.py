from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
from datetime import date

class Driver():
    """Driver Class"""

    def __init__(self, website, delay):
        """Initialize webdriver and class attributes"""
        
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.website = website
        self.delay = delay
    
    def open_website(self):
        """Open the screening tool in the webdriver"""

        self.driver.get(self.website)

    def clickable_xpath(self, xpath):
        """Return a clickable xpath element"""

        return WebDriverWait(self.driver, self.delay).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )

    def clickable_id(self, id):
        """Return a clickable id element"""

        return WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.ID, id))
            )
    
    def start_school_screening(self):
        """Click the start button on the homepage"""

        try:
            element = self.clickable_xpath('/html/body/div/div[1]/div[3]/main/div/div/div/div[3]/div[1]/button')     
            element.click()

        except TimeoutException:
            raise TimeoutException('Webdriver waited too long for a response. Try running the program again')
        
    def select_student(self):
        """Click the student button"""

        try:
            element = self.clickable_id('student')
            element.click()
            
        except TimeoutException:
           raise TimeoutException('Webdriver waited too long for a response. Try running the program again')
        
    def select_continue(self, xpath):
        """Click continue"""

        try:
            element = self.clickable_xpath(xpath)
            element.click()
       
        except TimeoutException:
            raise TimeoutException('Webdriver waited too long for a response. Try running the program again')

    def select_no(self, xpath):
        """Click No"""

        try:
            element = self.clickable_xpath(xpath)
            element.click()

        except TimeoutException:
            raise TimeoutException('Webdriver waited too long for a response. Try running the program again')
    
    def screenshot(self, filename):
        """Take a screenshot of the verified screen"""

        try:
            element = self.clickable_xpath('/html/body/div/div[1]/span/div[2]/main/div/div[1]/div/div')
            self.driver.save_screenshot(filename)

        except TimeoutException:
            raise TimeoutException('Webdriver waited too long for a response. Try running the program again')