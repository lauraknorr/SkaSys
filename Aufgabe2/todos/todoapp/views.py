from django.shortcuts import render, HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.

def home(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todotemps/uebersicht.html', context)

def neuesTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            titel = form.cleaned_data['titel']
            beschreibung = form.cleaned_data['beschreibung']
            tag = form.cleaned_data['tag']
            monat = form.cleaned_data['monat']
            jahr = form.cleaned_data['jahr']
            status = 0
            t = Todo(titel = titel, beschreibung = beschreibung, tag = tag,
                        monat = monat, jahr = jahr, status = status)
            t.save()
            form = TodoForm()
            return render(request, 'todotemps/neuesTodo.html',{'form': form})
        else:
            print("form not valid")
            print(form.errors)
    else:
        #wenn kein post, leeres form laden
        form = TodoForm()

    return render(request, 'todotemps/neuesTodo.html', {'form': form})

def bearbeitungTodo(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todotemps/bearbeitungTodo.html', context)

def impressum(request):
    return render(request, 'todotemps/impressum.html')

# def add_todo(request):
#     print("Form is submitted")
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             titel = form.cleaned_data['titel']
#             beschreibung = form.cleaned_data['beschreibung']
#             tag = form.cleaned_data['tag']
#             monat = form.cleaned_data['monat']
#             jahr = form.cleaned_data['jahr']
#             status = 0
#             t = Todo(titel = titel, beschreibung = beschreibung, tag = tag,
#                         monat = monat, jahr = jahr, status = status)
#             t.save()
#             form = TodoForm()
#             return render(request, 'todotemps/neuesTodo.html',{'form': form})
#         else:
#             print("form not valid")
#             print(form.errors)
#     else:
#         form = TodoForm()
#
#     return render(request, 'todotemps/neuesTodo.html', {'form': form})
