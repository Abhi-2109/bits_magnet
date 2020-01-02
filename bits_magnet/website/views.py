from django.shortcuts import render
from django.http import HttpResponse
from .models import person,awards

# Create your views here.

def index(request):
    person_list = person.objects.order_by('name')
    award = awards.objects.order_by('title')
    return render(request,'index.html', {'person': person_list,
                                         'awards':award,})
    #return HttpResponse("<H1>Hello World </H1>")