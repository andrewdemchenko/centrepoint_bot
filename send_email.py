import smtplib


def email(email):
    support = 'nordstone333@gmail.com'
    user = email

    password = '0958738602'

    msg = '\r\n'.join([
        'From: {}'.format(support),
        'To: {}'.format(user),
        'Subject: User Support',
        '',
        'This user {} have some questions. Contact it, please.'.format(user)
    ])

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.login(support, password)
    server.sendmail(support, [user], msg)
    server.quit()