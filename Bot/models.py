from django.db import models

# Create your models here.


class Users(models.Model):
	chat_id = models.CharField(max_length=100)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return str(self.chat_id)

