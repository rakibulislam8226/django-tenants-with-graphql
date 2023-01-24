from django.views.generic import TemplateView
from django.urls import path
from client import views as client_views

urlpatterns = [
    path('',TemplateView.as_view(template_name="client/index.html"),name='client_index'),
    path('list/api/', client_views.ClientList.as_view()),
    path('details/api/<int:pk>/', client_views.ClientDetail.as_view(),name='clientDetailApi'),
]
