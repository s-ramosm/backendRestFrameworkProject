import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email (receiver,content,subject,type= 'plain'):
    mail_content =content
    
    #The mail addresses and password
    sender_address = 'pruebas.bd.14@gmail.com'
    sender_pass = 'Pruebas2022*'
    receiver_address = receiver

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] =subject   #The subject line
    
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, type))
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls() #enable security
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')