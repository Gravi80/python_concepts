import smtplib
import imapclient

# https://automatetheboringstuff.com/chapter16/
print("******** Send emails ********")
# https://sendgrid.com/free/
conn = smtplib.SMTP('smtp.gmail.com', 587)
mail_username = ''
# https://support.google.com/accounts/answer/185833?hl=en
mail_password = ''
print(conn.ehlo())
print(conn.starttls())
# https://myaccount.google.com/lesssecureapps?pli=1
print(conn.login(mail_username, mail_password))
# You can send multiple mails, 'sendmail' returns a dictionary which contains failed emails
conn.sendmail(mail_username, mail_username, 'Subject: So long...\n\n'
                                            'Dear Ravi,\n So long, and thanks for all the fish. \n\n From Ravi')
conn.quit()

print("******** Check email inbox ********")
# easy_install pyzmail
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# https://myaccount.google.com/lesssecureapps?pli=1
print(conn.login(mail_username, mail_password))
print(list(map(lambda row: row[2], conn.list_folders())))
print(conn.select_folder('INBOX', readonly=True))
mail_ids = conn.search(['FROM', 'no-reply@swiggy.in'])
print(mail_ids)
raw_message = conn.fetch(mail_ids[-1], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(raw_message[mail_ids[-1]][b'BODY[]'])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))

print(message.text_part.charset)
print(message.text_part)  # plain text part of body
print(message.html_part)  # html part of body
print(message.text_part.get_payload().decode('utf-8'))
conn.close_folder()

print("\n******** Delete email ********")
print(conn.select_folder('INBOX', readonly=False))
mail_ids = conn.search(['ON', '09-Aug-2020'])
print(mail_ids)
conn.delete_messages(mail_ids)
