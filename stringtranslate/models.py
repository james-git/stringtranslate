from django.db import models
from django.forms import ModelForm, Textarea
from django.utils import timezone


class AppSet(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False, null=False)

	def __str__(self):
		return self.name
		
	
class LangCode(models.Model):
	code = models.CharField(max_length=8, unique=True, blank=False, null=False)

	def __str__(self):
		return self.code
		
		
class StringKey(models.Model):
	string_key = models.CharField(max_length=50, unique=True, blank=False, null=False)
	
	def __str__(self):
		return self.string_key
	

class StringTable(models.Model):
	app_set = models.ForeignKey('AppSet')
	lang_code = models.ForeignKey('LangCode')	
	string_key = models.ForeignKey('StringKey')
	string_content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		unique_together = ('app_set', 'string_key', 'lang_code')
	
	def commit(self):
		self.modified_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.string_content
		
		
class AppSetForm(ModelForm):
	class Meta:
		model = AppSet
		fields = '__all__'
		
		
class LangCodeForm(ModelForm):
	class Meta:
		model = LangCode
		fields = '__all__'
		
		
class StringKeyForm(ModelForm):
	class Meta:
		model = StringKey
		fields = '__all__'
	
	
class StringTableForm(ModelForm):
	class Meta:
		model = StringTable
		# fields = '__all__'
		exclude = ['app_set', 'lang_code', 'created_date', 'modified_date']
		widgets = {
			'string_key': Textarea(attrs={'cols': 50, 'rows': 1}),
			'string_content': Textarea(attrs={'cols': 80, 'rows': 5}),
		}
