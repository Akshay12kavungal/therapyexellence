from django.core.mail import send_mail

from django.conf import settings

def send_forget_password_mail(Email,token):
	
	subject='your forget password link'
	message=f'hi,http://127.0.0.1:8000/password-reset-confirm/{token}/'
	email_from=EMAIL_HOST_USER
	recipient_list=[Email]
	send_mail(subject,message,email_from,recipient_list)
	return True