from django.shortcuts import render, HttpResponse
from .forms import TodoForm

# Create your views here.
def home(request):
    return render(request, 'todotemps/uebersicht.html')

def neuesTodo(request):

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            titel = form.cleaned_data['titel']
            beschreibung = form.cleaned_data['Beschreibung']
            tag = form.cleaned_data['tag']
            monat = form.cleaned_data['monat']

    form = TodoForm()
    return render(request, 'todotemps/neuesTodo.html')

def bearbeitungTodo(request):
    return render(request, 'todotemps/bearbeitungTodo.html')

def impressum(request):
    return render(request, 'todotemps/impressum.html')
