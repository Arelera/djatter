from django.shortcuts import render
from search.models import Search

def index(req):
    return render(req, 'djatter/index.html', {'searches': Search.objects.order_by('-search_date')})