from django.urls import path
from .views import pessoas_list, pessoas_new, pessoas_update

urlpatterns = [
    path('list/', pessoas_list, name='pessoa_list'),
    path('new/', pessoas_new, name='pessoa_new'),
    path('update/<int:id>/', pessoas_update, name='pessoa_update')
]