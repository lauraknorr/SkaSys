from django.shortcuts import render, HttpResponse, redirect
from .models import Todo
from .forms import TodoForm
from django.forms.models import model_to_dict
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

def bearbeitungTodo(request, id):
    todo = Todo.objects.get(pk = id)
    if request.method == 'POST':
        todo.titel = request.POST.get('titel')
        todo.beschreibung = request.POST.get('beschreibung')
        todo.tag = request.POST.get('tag')
        todo.monat = request.POST.get('monat')
        todo.jahr = request.POST.get('jahr')
        todo.status = request.POST.get('status')
        todo.save()
        data = model_to_dict(todo)

        context = {
            'todo': todo,
            'form' : TodoForm(initial = data),

        }
        return render(request, 'todotemps/bearbeitungTodo.html', context)

    data = model_to_dict(todo)

    context = {
        'todo': todo,
        'form' : TodoForm(initial = data),

    }
    return render(request, 'todotemps/bearbeitungTodo.html',context)

def impressum(request):
    return render(request, 'todotemps/impressum.html')

def delete_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(pk = id)
        todo.delete()

    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todotemps/uebersicht.html', context)
