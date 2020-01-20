from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):

    # Query the data for the top 5 liked categories
    category_list = Category.objects.orderby('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'name': 'Fabrizio Catinella'}
    return render(request, 'rango/about.html', context=context_dict)
