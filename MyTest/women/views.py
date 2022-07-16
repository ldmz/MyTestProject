from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(f"Страница Women")

def categories(request, catid):
    return HttpResponse(f"<h1>Структура по каталогам</h1><p>{catid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")