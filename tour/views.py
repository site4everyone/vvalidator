from django.shortcuts import render
from .models import Article


def home(request):
    query = ''
    try:
        query = request.GET['term']
    except:
        pass
    if query != '':
        lst = Article.objects.filter(title=query)
    else:
        lst = Article.objects.all()
    return render(request, 'index.html', {"arts": lst})
