import datetime
from django.shortcuts import render

# Create your views here.

def es_if(request):
    context = {
        'var1': 10,
        'var2': 20,
        'var3': 15,
    }
    return render(request, 'es_if.html', context)

def if_else_elif(request):
    context = {
        'var1': 10,
        'var2': 20,
        'var3': 15,
    }
    return render(request, 'if_else_elif.html', context)

def es_for(request):
    dic = { 'list1': [1, datetime.date(2026,7,15), 'Never give up!!'],'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "es_for.html", dic)