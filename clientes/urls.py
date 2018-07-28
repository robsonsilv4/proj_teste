from django.urls import path
from .views import pessoas_list

urlpatterns = [
    path('list', pessoas_list)
]
