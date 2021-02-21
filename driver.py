from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import date

class Driver():
    """ Driver Class """

    def __init__(self, website, delay):
        self.driver = webdriver.Firefox(executable_path='webdriver/geckodriver.exe')
        self.website = website
        self.delay = delay
    
    def open_website(self):
        self.driver.get(self.website)
        return 'Opening website...'

    def clickable_xpath(self, xpath):
        return WebDriverWait(self.driver, self.delay).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
            )

    def clickable_id(self, id):
        return WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.ID, id))
            )
    
    def start_school_screening(self):
        while True:
            try:
                element = self.clickable_xpath('/html/body/div/div[1]/div[3]/main/div/div/div/div[3]/div[1]/button')     
                if element:
                    element.click()
                    return 'Started Screening...'
                    break

            except TimeoutException:
                return 'Took too long... Trying again...'
        
    def select_student(self):
        while True:
            try:
                element = self.clickable_id('student')
                if element:
                    element.click()
                    return 'Selected Student...'
                    break

            except TimeoutException:
                return 'Took too long... Trying again...'

    def select_continue(self, xpath):
        while True:
            try:
                element = self.clickable_xpath(xpath)
                if element:
                    element.click()
                    return 'Continued...'
                    break

            except TimeoutException:
                return 'Took too long... Trying again...'

    def select_no(self, xpath):
        while True:
            try:
                element = self.clickable_xpath(xpath)
                print(element)

            except TimeoutException:
                return 'Took too long... Trying again...'

            if element:
                element.click()
                return 'Selected No...'
                break
    
    def screenshot(self, filepath=None):
        while True:
            try:
                element = self.clickable_xpath('/html/body/div/div[1]/span/div[2]/main/div/div[1]/div/div')
                if element:
                    if filepath:
                        self.driver.save_screenshot(filepath)
                        return f"Saved Screenshot as {filepath}"
                    else:
                        date_today = date.today()
                        filename = str(date_today) + '.png'
                        self.driver.save_screenshot(f"screenshots/{filename}")
                        return f"Saved Screenshot as {filename}"
                    break

            except TimeoutException:
                return 'Took too long... Trying again...'

