from sweet_tenant.views import Index
from django.urls import path
from sweet_tenant import views as sweetTenantViews

urlpatterns = [
    path('',Index.as_view(),name='tenant_index'),
    path('tenant/list/api/', sweetTenantViews.SweetList.as_view()),
    path('tenant/details/api/<int:pk>/', sweetTenantViews.SweetDetail.as_view(),name='SweetDetailApi'),
]
