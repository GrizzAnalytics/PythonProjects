import smtplib

to = input("Enter ther receivers email id : \n")

content = input("Enter the content to send : \n")

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('kayin.patton@gmail.com', 'Panthers2_2')
	server.sendmail('kumadagrizzly@gmail.com', to, content)
	server.close()

sendEmail(to, content)