from django.conf.urls import url
from .views import (
    TodoListView
)
from . import views

urlpatterns = [
    url(r'^$', TodoListView.as_view(), name='todo-uebersicht'),
    url(r'^uebersicht', TodoListView.as_view(), name='todo-uebersicht'),
    url(r'^neuesTodo',views.neuesTodo,name='todo-neu'),
    url(r'^bearbeitungTodo', views.bearbeitungTodo, name='todo-bearbeitung'),
    url(r'^impressum', views.impressum, name='todo-impressum'),
]
