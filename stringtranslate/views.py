from django.shortcuts import render

def post_list(request):
    return render(request, 'stringtranslate/post_list.html', {})