import sys
from smtplib import SMTP
from email.message import EmailMessage

sender = 'sender@mail.ru'
host = 'mail.spbu.ru'
port = 25


def main(receiver, text):
    msg = EmailMessage()
    msg['Subject'] = ''
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(text)
    with SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.sendmail(sender, receiver, msg.as_string())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Specify a receiver and a message to send', file=sys.stderr)
    else:
        main(sys.argv[1], sys.argv[2])

