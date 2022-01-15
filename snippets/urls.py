from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

app_name = 'snippet'

urlpatterns = [
    path('', views.snippet_list, name='view'),
    path('<int:pk>/', views.snippet_detail, name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
