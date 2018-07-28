from django.urls import path
from .views import pessoas_list, pessoas_new

urlpatterns = [
    path('list/', pessoas_list, name='pessoa_list'),
    path('new/', pessoas_new, name='pessoa_new'),
]