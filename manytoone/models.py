from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	
	# user=models.ForeignKey(User,on_delete=models.CASCADE)

	#  Cannot delete user with PROTECT 
	# user=models.ForeignKey(User,on_delete=models.PROTECT)

	# It will set the User to Null if we delete user 
	user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	post_title=models.CharField(max_length=100)
	post_cat=models.CharField(max_length=100)
	post_publish_date=models.DateField()
