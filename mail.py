import smtplib
import config


def send_email(name, receiver):
    subject = "Anxiety Test"
    msg = name + " might be suffering from anxiety."
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS,receiver, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")



#name = 'Arnav'
#receiver="pragyashashwati5@gmail.com"
#send_email(name, receiver)
