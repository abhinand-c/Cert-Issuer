# Mail modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class EmailMessage:
    def __init__(self):
        self.message = MIMEMultipart("alternative")

    def attach(self, path, name=None):
        # attachments for the mail
        if name is None:
            name = path
        attach_file = open(path, 'rb')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)  # encode the attachment

        # add payload header with filename
        payload.add_header('Content-Disposition',
                           "attachment; filename= %s" % name)
        self.message.attach(payload)

    def send_mail(self, subject, text_content, sender, recipient, mail_session, html_message=None):
        self.message['From'] = sender
        self.message['To'] = recipient
        self.message['Subject'] = subject
        self.message.attach(MIMEText(text_content, 'plain'))
        if html_message:
            self.message.attach(MIMEText(html_message, 'html'))
        text = self.message.as_string()
        mail_session.sendmail(sender, self.message.get('To'), text)


class Mailer:
    def __init__(self, HOST_MAIL, HOST, HOST_PASSWORD, PORT):
        self.HOST_MAIL = HOST_MAIL
        self.HOST = HOST
        self.HOST_PASSWORD = HOST_PASSWORD
        self.PORT = PORT
        self.message = MIMEMultipart("alternative")

    def start_session(self):
        self.session = smtplib.SMTP(self.HOST, self.PORT)
        self.session.starttls()  # enable security
        # login with mail_id and password
        self.session.login(self.HOST_MAIL, self.HOST_PASSWORD)
        return self.session

    def end_session(self):
        self.session.quit()
