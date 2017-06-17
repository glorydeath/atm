import smtplib
from email.mime.text import MIMEText

smtp_server_addr = 'smtp.live.com'
smtp_server_port = 587

smtp_username = 'email_addr'
smtp_password = 'smtp_pwd'

from_addr = 'email_addr'
to_addr = 'email_addr'


def send_email(msg):
    msg = MIMEText(msg)

    msg['Subject'] = "Stock alert!"
    msg['From'] = from_addr
    msg['To'] = to_addr
    mail_server = smtplib.SMTP(smtp_server_addr, smtp_server_port)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(smtp_username, smtp_password)
    mail_server.sendmail(from_addr, [to_addr], msg.as_string())
    mail_server.quit()

# send_email('cross up')
