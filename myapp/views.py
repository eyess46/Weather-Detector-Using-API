from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Subscriber, Newsletter
from django.contrib import messages
import json
import urllib.request


# Create your views here.



def index(request):
    if request.method == "POST":
        city = request.POST['city']
        api_key = '960b16bf6ec18fd0b647a32ef468c593'  
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=960b16bf6ec18fd0b647a32ef468c593'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            "country": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data})
