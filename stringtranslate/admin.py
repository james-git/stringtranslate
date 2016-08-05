from django.contrib import admin

from .models import AppSet
from .models import LangCode
from .models import StringKey
from .models import StringTable

# Register your models here.

admin.site.register(AppSet)
admin.site.register(LangCode)
admin.site.register(StringKey)
admin.site.register(StringTable)
