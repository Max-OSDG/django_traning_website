from django.http import HttpResponse
from django.shortcuts import render



def first_page(request):
    a = '<h1> Hellow world </h1>'
    text = 'New Text'
    return render(request, "./index.html", {
        'a': a,
        'Text': text
    })