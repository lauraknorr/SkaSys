from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^uebersicht', views.home),
    url(r'^neuesTodo',views.neuesTodo),
    url(r'^bearbeitungTodo', views.bearbeitungTodo),
    url(r'^impressum', views.impressum),
]
