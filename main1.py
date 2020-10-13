import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mayemail1988@gmail.com"  # Enter your address
receiver_email = "menezeslage@gmail.com"  # Enter receiver address
password = "tercioapolinario"
message = """\
Subject: TESTE APP

Fala Guilherme, um teste aqui!."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
