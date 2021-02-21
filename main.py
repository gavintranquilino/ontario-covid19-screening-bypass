from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Driver():
    """ Driver Class """

    def __init__(self, driver, website, delay):
        self.driver = driver
        self.website = website
        self.delay = delay
    
    def open_website(self):
        self.driver.get(self.website)
    
    def start_school_screening(self):
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div/div[1]/div[3]/main/div/div/div/div[3]/div[1]/button'))
                ).click()
        except TimeoutException:
            print('Took too long')
        
    def select_student(self):
        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, 'student'))).click()
        except TimeoutException:
            print('Took too long')

    def select_continue(self, xpath):
        try:
            WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except TimeoutException:
            print('Took too long')

    def select_no(self, xpath):
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except TimeoutException:
            print('Took too long')
    
def main():
    driver = Driver(
        driver = webdriver.Firefox(executable_path='webdriver/geckodriver.exe'), 
        website = 'https://covid-19.ontario.ca/school-screening/',
        delay = 10
        )

    print('Opening Website...')
    driver.open_website()

    print('Screening Starting...')
    driver.start_school_screening()

    print('Selecting Student...')
    driver.select_student()

    print('Selecting Continue...')
    driver.select_continue('/html/body/div/div[1]/div[2]/main/div/div/div/div[2]/button')

    for i in range(4):
        print(f"No I have not #{i+1}...")
        driver.select_no('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button[1]')

    print('Selecting Continue...')
    driver.select_continue('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button')
    
    print('No I do not live with anyone with symptoms...')
    driver.select_no('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button[1]')

if __name__ == '__main__':
    main()