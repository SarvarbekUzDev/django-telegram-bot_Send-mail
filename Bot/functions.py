from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

import requests
import os

from data.config import ADMINS, BOT_TOKEN, RECEIVING_MAILS
from .models import Users



# User data
def user_data_(get_json, admin_id=False):
	try:
		try:
			chat_id = get_json['message']['chat']['id']
		except KeyError:
			chat_id = get_json['callback_query']['from']['id']

		# Is Admin 
		if admin_id:
			for admin in ADMINS:
				if str(admin) == str(chat_id):
					return True

			return False

		# Get
		user = Users.objects.get(chat_id=chat_id)

		return {'user':user, 'is_admin':True}
	except:
		return {'user':False, 'is_admin':False}



# send mail
def custom_send_mail(image, title, description):
	from_email = settings.EMAIL_HOST_USER
	to_email  = RECEIVING_MAILS # type list

	
	msg = EmailMultiAlternatives(title, description, from_email, to_email)
	msg.attach_alternative(description, "text/html")
	msg.attach_file(image)
	msg.send()


# Save Image 
def save_image(file_id, chat_id="None"):
	file_path = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={file_id}").json()['result']['file_path']
	response = requests.get(f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}")
	# image path
	path = f"static/images/{file_id}-{chat_id}.jpg"
	# save image
	with open(path, "wb") as image:
	    image.write(response.content)


	return path