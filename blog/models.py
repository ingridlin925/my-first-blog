from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	"""docstring for Post"models.Modelf __init__(self, arg):
		super Post,models.Model.__init__()
		self.arg = arg"""

	author = models.ForeignKey('auth.User')	#a link to another model
	title = models.CharField(max_length=200)	#define text with a limited number of characters.
	text = models.TextField() 					#long text without a limit
	created_date = models.DateTimeField(
		default=timezone.now)					#date and time
	publised_date = models.DateTimeField(blank=True , null=True)

	def publised(self):
		self.published_date = timezone.now
		self.save()

	def __str__(self):
		return self.title

		