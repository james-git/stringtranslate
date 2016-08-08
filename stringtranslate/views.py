# from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import AppSet, LangCode, StringKey, StringTable


def post_list(request):
    # return render(request, 'stringtranslate/post_list.html', {})
	return render_to_response('stringtranslate/post_list.html', {})
	
def view_string_table(request):
	return render_to_response('stringtranslate/view_string_table.html', {})