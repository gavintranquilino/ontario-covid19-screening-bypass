import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
import os

class Email(object):
    """Email Class"""

    def __init__(self, host, port):
        """Set class attributes"""

        self.msg = EmailMessage()
        self.names = []
        self.emails = []
        self.smtp = smtplib.SMTP(host=host, port=port)
    
    def get_contacts(self):
        """Put all contacts from contacts.txt to a list"""

        try:
            with open ('templates/default_contacts.txt', mode='r', encoding='utf-8') as contacts_file:
                for contact in contacts_file:
                    self.names.append(contact.split()[0]) # Put names in names list
                    self.emails.append(contact.split()[1]) # Put emails in emails list
        except:
            with open ('templates/contacts.txt', mode='r', encoding='utf-8') as contacts_file:
                for contact in contacts_file:
                    self.names.append(contact.split()[0]) # Put names in names list
                    self.emails.append(contact.split()[1]) # Put emails in emails list
            
    
    def read_template(self):
        """Read message template from messsage.txt"""
        try:
            with open('templates/default_message.txt', mode='r', encoding='utf-8') as template_file:
                template_content = template_file.read()
            self.message_template = Template(template_content)
        except:
            with open('templates/message.txt', mode='r', encoding='utf-8') as template_file:
                template_content = template_file.read()
            self.message_template = Template(template_content)
         
    def setup_smtp_server(self, email_address, password):
        """Initialize SMTP server"""

        self.smtp.starttls()
        self.smtp.login(email_address, password)

    def set_person_name(self, name):
        """Set the contact name in message.txt"""

        return self.message_template.substitute(PERSON_NAME=name.title())

    def get_img(self, filepath):
        """Return MIMEImage from screenshots folder"""

        with open(filepath, mode='rb') as file:
            img_data = file.read()
            return MIMEImage(img_data, name=os.path.basename(filepath)) 

    def send_email_to_each_contact(self, email_address, email_subject, image_path):
        """Send an email through SMTP to each contact"""
        
        for name, email in zip(self.names, self.emails):
            mime = MIMEMultipart()

            message = self.set_person_name(name)

            mime['From']=email_address
            mime['To']=email
            mime['Subject']=email_subject

            mime.attach(MIMEText(message, 'plain'))
            mime.attach(self.get_img(image_path))

            self.smtp.send_message(mime)

            del mime
