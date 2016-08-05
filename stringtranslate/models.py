from django.db import models
from django.utils import timezone


class AppSet(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name
		
	
class LangCode(models.Model):
	code = models.CharField(max_length=8, unique=True)

	def __str__(self):
		return self.code
		
		
class StringKey(models.Model):
	app_set = models.ForeignKey('AppSet', blank=False, null=False)
	string_key = models.CharField(max_length=50, unique=True)
	
	def __str__(self):
		return self.string_key
	

class StringTable(models.Model):
	string_key = models.ForeignKey('StringKey')
	lang_code = models.ForeignKey('LangCode', blank=False, null=False)
	string_content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		unique_together = ('string_key', 'lang_code')
	
	def save(self):
		self.modified_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.string_content
		