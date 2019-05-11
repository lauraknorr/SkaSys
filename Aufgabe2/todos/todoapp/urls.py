from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^uebersicht', views.home, name='todo-uebersicht'),
    url(r'^neuesTodo',views.neuesTodo, name='todo-neu'),
    url(r'^bearbeitungTodo', views.bearbeitungTodo, name='todo-bearbeitung'),
    url(r'^impressum', views.impressum, name='todo-impressum'),
]
