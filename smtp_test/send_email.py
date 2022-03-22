import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'abhilash.haranadha@gmail.com'
password = ''



def send_mail(text='Email Body', subject='Congratulations!',from_email='JACKPOT <abhilash.haranadha@gmail.com>', to_emails=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    
    txt_part = MIMEText(text,'plain')
    # msg.attach(txt_part)
    
    html_part = MIMEText('<div><h1>You Won a lottery of rupees 1 lakhs !!!!</h1><a href="https://www.youtube.com/watch?v=XqZsoesa55w">Click Here to Claim</a></div>',"html")
    msg.attach(html_part)
    
    msg_str = msg.as_string()
    #login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)   
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails,msg_str)
    server.quit()
