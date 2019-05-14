from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'todo-uebersicht'),
    path('uebersicht', views.home, name = 'todo-uebersicht'),
    path('neuesTodo',views.neuesTodo, name='todo-neu'),
    path('bearbeitungTodo/<int:id>', views.bearbeitungTodo, name='todo-bearbeitung'),
    path('impressum', views.impressum, name='todo-impressum'),
    path('delete_todo/<int:id>',views.delete_todo, name='delete_todo'),
]
