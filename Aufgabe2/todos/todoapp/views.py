from django.shortcuts import render, HttpResponse
form .forms import TodoForm

# Create your views here.
def home(request):
    return render(request, 'todotemps/uebersicht.html')

def neuesTodo(request):
    return render(request, 'todotemps/neuesTodo.html')

def bearbeitungTodo(request):
    return render(request, 'todotemps/bearbeitungTodo.html')

def impressum(request):
    return render(request, 'todotemps/impressum.html')
