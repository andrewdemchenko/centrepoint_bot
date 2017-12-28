import smtplib


def email(email):
    bot = 'centrepointbot@gmail.com'
    user = email
    support = 'nordstone333@gmail.com'

    password = 'qwerty678606'

    msg = '\r\n'.join([
        'From: {}'.format(bot),
        'To: {}'.format(support),
        'Subject: Centrepoint Bot Report',
        '',
        'Hi! {} have some questions. Write to him, please.'.format(user)
    ])

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.login(bot, password)
    server.sendmail(bot, [support], msg)
    server.quit()