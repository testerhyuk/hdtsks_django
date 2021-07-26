from django.urls import path
from django.views.generic import TemplateView

from articleapp import views

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('select_date/', TemplateView.as_view(template_name='articleapp/select_date.html'), name='select_date'),
    path('table_list/', views.table_list, name='table_list')
]