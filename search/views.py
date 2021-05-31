import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from djatter.settings import OWM_KEY
from .models import Search

def index(req):
    location = req.POST['location']
    return HttpResponseRedirect(reverse('search:details', args=[location]))

def details(req, location):    
    data = requests.get(
        'http://api.openweathermap.org/data/2.5/weather', params={'units': 'metric', 'q': location, 'appid': OWM_KEY}
    ).json()


    if (data['cod'] == '404'):
        search = Search(query=location, is_valid=False)
        search.save()
        return render(req, 'djatter/index.html', {'error': 'Location not found.'})
    
    search = Search(query=location, is_valid=True)
    search.save()
    return render(req, 'search/details.html', {'data': data, 'searches': Search.objects.order_by('-search_date')})

