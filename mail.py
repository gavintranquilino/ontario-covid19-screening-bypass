import smtplib
from email.message import EmailMessage
from string import Template

class Email(object):
    """ Email Class """

    def __init__(self, host, port):
        self.msg = EmailMessage()
        self.names = []
        self.emails = []
        self.smtp = smtplib.SMTP(host=host, port=port)
    
    def get_contacts(self, filename):
        with open (filename, mode='r', encoding='utf-8') as contacts_file:
            for contact in contacts_file:
                self.names.append(contact.split()[0])
                self.emails.append(contact.split()[1])
        return self.names, self.emails 
    
    def read_template(self, filename):
        with open(filename, mode='r', encoding='utf-8') as template_file:
            template_content = template_file.read()
        return Template(template_content)
    
    def setup_smtp_server(self, address, password):
        self.smtp.starttls()
        self.login(address, password)
