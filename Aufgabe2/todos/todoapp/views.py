from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.

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
