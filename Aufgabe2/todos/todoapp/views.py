from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.

todos = [
    {
        'titel':'Todo Nr 1',
        'beschreibung':'Todos auflisten können',
        'deadline':'14 Mai 2019',
        'status':20
    },
    {
        'titel':'Todo Nr 2',
        'beschreibung':'Todos löschen können',
        'deadline':'14 Mai 2019',
        'status':75
    }
]



def home(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todotemps/uebersicht.html', context)

def neuesTodo(request):
    return render(request, 'todotemps/neuesTodo.html')

def bearbeitungTodo(request):
    return render(request, 'todotemps/bearbeitungTodo.html')

def impressum(request):
    return render(request, 'todotemps/impressum.html')
