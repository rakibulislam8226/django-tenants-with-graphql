from django.urls import path
from sweet_shared import views as sweetShared_views

urlpatterns = [
    path('shared/api/', sweetShared_views.SweetSharedList.as_view()),
    path('shared/details/api/<int:pk>/', sweetShared_views.SweetSharedDetail.as_view(),name='clientDetailApi'),
]
