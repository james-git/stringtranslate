# from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import AppSet, LangCode, StringKey, StringTable


def post_list(request):
    # return render(request, 'stringtranslate/post_list.html', {})
	return render_to_response('stringtranslate/post_list.html', {})
	
def view_string_table(request):
	if 'appset_id' in request.POST:
		appset_id = request.POST['appset_id']
		langcode_id = request.POST['langcode_id']
		
		appset = AppSet.objects.get(id=appset_id)
		langcode = LangCode.objects.get(id=langcode_id)
		
		stringtable = StringTable.objects.filter(app_set=appset, lang_code=langcode)
		
		return render_to_response('stringtranslate/view_string_table01.html', locals())
	else:
		appset = AppSet.objects.all()
		langcode = LangCode.objects.all()
	
		return render_to_response('stringtranslate/view_string_table.html', locals())