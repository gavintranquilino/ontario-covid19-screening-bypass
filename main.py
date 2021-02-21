import driver as webdriver
    
def main():
    driver = webdriver.Driver( 
        website = 'https://covid-19.ontario.ca/school-screening/',
        delay = 3
        )

    print(driver.open_website())

    print(driver.start_school_screening())

    print(driver.select_student())

    print(driver.select_continue('/html/body/div/div[1]/div[2]/main/div/div/div/div[2]/button'))

    for i in range(4):
        print(f"No I have not #{i+1}...")
        driver.select_no('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button[1]')

    print(driver.select_continue('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button'))
    
    print(driver.select_no('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button[1]'))

    print(driver.screenshot())

    driver.driver.close()

if __name__ == '__main__':
    main()