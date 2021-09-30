from jinja2 import Environment, FileSystemLoader
from api import CertProcessor
from mailer import EmailMessage, Mailer
from decouple import config
import pandas as pd
import csv


HOST_MAIL = config("HOST_MAIL")
HOST = config("HOST")
HOST_PASSWORD = config("HOST_PASSWORD")
PORT = config("PORT")

#####################
# EDIT THESE VARIABLES

template_path = "Certificate_Design_Part.png"
font_path = "Montserrat-Medium.ttf"
font_size = 162
pos = (2338, 1730)

excel_file = 'CertificatesList.xlsx'
sheet_name = 0

log_file_path = 'log.csv'

# Mail Content
attachment_filename = "Actuator_Cert.pdf"
title = "Actuator'21 Certificate"
mail_subject = "CERTIFICATE: Actuator'21 Participation."
mail_message = (
    "Hope this email finds you in good health and high spirits."

    "\n\nCongratulations on the successful completion of “Actuator’21,The Beginner’s Workshop”"
    " conducted virtually from May 23,2021 to May 30,2021 by Robocek GCEK. "

    "\n\nThank you for your coordination which made the event a grant success even in the online mode."
    "And here in, we have attached the digital copy of your ‘Certificate of Participation’. "
    "In case of any discrepancies, feel free to contact us. "
    "We expect your support and devoted participation in the further journey of Robocek. "
)

# END #
#######


file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('message.html')


mail_content = "Hello, {Name}\n" + mail_message + "\nThank You"

df = pd.read_excel(excel_file, sheet_name=sheet_name)
df.head()

mailer = Mailer(HOST_MAIL, HOST, HOST_PASSWORD, PORT)
mail_session = mailer.start_session()

log_file = open(log_file_path, mode='w', newline='')
log_writer = csv.writer(log_file)

for index, person in df.iterrows():
    name = person['Name'].upper().strip()
    print(f"\n{index} : {name}", end=" - ")

    cert = CertProcessor(template_path, font_path, font_size)
    cert.add_text(name, pos)
    cert.save_pdf("temp")

    mail = EmailMessage()
    mail.attach("temp.pdf", attachment_filename)
    name = person['Name'].upper().strip()

    html_output = template.render(message=mail_message, name=name)
    text_content = mail_content.format(**person)

    mail.send_mail(subject=mail_subject, text_content=text_content, sender=HOST_MAIL,
                   recipient=person['Mail'], html_message=html_output, mail_session=mail_session)
    log_writer.writerow([name,  person['Mail'], "issued"])
    print("Mail Sent successful")
