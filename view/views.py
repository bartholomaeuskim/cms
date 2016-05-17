from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django import forms

# Create your views here.
def index(request, menu_id=None):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    menu = ("eds", "arrival_date", "kaida", "sagai", "stock", "sagai_stock")
    if menu_id:
        if menu_id in menu:
            return render(request, 'pages/index.html', {'id' : menu_id})
        else:
            return HttpResponse(None)
    else:
        return render(request, 'pages/index.html')
