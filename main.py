import driver as webdriver
import mail
import json
from datetime import date
    
def get_filename():
    return 'screenshots/' + str(date.today()) + '.png'

def handle_website():
    driver = webdriver.Driver( 
    website = 'https://covid-19.ontario.ca/school-screening/',
    delay = 10
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

    print(driver.screenshot(get_filename()))

    driver.driver.close()

def handle_email():
    email = mail.Email('smtp.office365.com', 587)
    print('SMTP Connection Complete...')

    print(email.get_contacts('templates/contacts.txt'))

    print(email.read_template('templates/message.txt'))

    with open('config.json', mode='r', encoding='utf-8') as config_file:
        data = json.load(config_file)
        email_address = data['address']
        password = data['password']
        email.setup_smtp_server(email_address, password)
        email.send_email_to_each_contact(
            email_address=email_address, 
            email_subject='COVID-19 Screening', 
            image_path=get_filename()
            )
    
    print('Email(s) Sent!')

def main():
    handle_website()
    handle_email()

if __name__ == '__main__':
    main()